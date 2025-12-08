import sys
import requests
from config import HCCLinksConfig, HCCLinksCollection, HCCLinksItem

__all__ = [ "BaseRequest", "HeadRequest", "GetRequest" ]

def map_attr(source_obj, attr_name, default_value):
    if hasattr(source_obj, attr_name):
        return getattr(source_obj, attr_name)
    else:
        return default_value

class BaseRequest(object):
    def __init__(self, hccl_item):
        if not isinstance(hccl_item, HCCLinksItem):
            raise TypeError("First positional arg must be of class HCCLinksItem")
        if hccl_item.min_status < 200:
            raise ValueError("Values of minStatus < 200 are unsupported")
        if hccl_item.max_status > 599:
            raise ValueError("Values of maxStatus > 599 are unsupported")
        self.description = map_attr(hccl_item, 'description', "[No description provided]")
        self.comment = map_attr(hccl_item, 'comment', None)
        self.url = map_attr(hccl_item, 'url', None)
        self.method = map_attr(hccl_item, 'method', 'HEAD')
        self.min_status = map_attr(hccl_item, 'min_status', None)
        self.max_status = map_attr(hccl_item, 'max_status', None)
        self.location_header_substr = map_attr(hccl_item, 'location_header_substr', None)
        self.content_type_starts_with = map_attr(hccl_item, 'content_type_starts_with', None)

class HeadRequest(BaseRequest):
    def __init__(self, hccl_item):
        super().__init__(hccl_item)
        if hasattr(hccl_item, 'text_success_substr'):
            raise ValueError("A HEAD request cannot have a textSuccessSubstr property")
        if hasattr(hccl_item, 'text_failure_substr'):
            raise ValueError("A HEAD request cannot have a textFailureSubstr property")

    def check(self):
        response = requests.head(self.url)
        if response.status_code < self.min_status:
            return { "url": self.url, "pass": False, "result": f"HEAD response status was {response.status_code} but status must be >= {self.min_status}" }
        if response.status_code > self.max_status:
            return { "url": self.url, "pass": False, "result": f"HEAD response status was {response.status_code} but status must be <= {self.max_status}" }
        if self.location_header_substr != None and self.location_header_substr not in response.headers['location']:
            return { "url": self.url, "pass": False, "result": f"HEAD response Location header did not contain substring {self.location_header_substr}" }
        if hasattr(response.headers, 'content-type') and self.content_type_starts_with != None and not response.headers['content-type'].startswith(self.content_type_starts_with):
            return { "url": self.url, "pass": False, "result": f"HEAD response Content-type header did not start with {self.content_type_starts_with}" }
        
        # If we got this far, it passes
        return { "url": self.url, "pass": True }

class GetRequest(BaseRequest):
    def __init__(self, hccl_item):
        super().__init__(hccl_item)
        self.text_success_substr = map_attr(hccl_item, 'text_success_substr', None)
        self.text_failure_substr = map_attr(hccl_item, 'text_failure_substr', None)
    
    def check(self):
        response = requests.get(self.url)
        if response.status_code < self.min_status:
            return { "url": self.url, "pass": False, "result": f"GET response status was {response.status_code} but status must be >= {self.min_status}" }
        if response.status_code > self.max_status:
            return { "url": self.url, "pass": False, "result": f"GET response status was {response.status_code} but status must be <= {self.max_status}" }
        if self.location_header_substr != None and self.location_header_substr not in response.headers['location']:
            return { "url": self.url, "pass": False, "result": f"GET response Location header did not contain substring {self.location_header_substr}" }
        if hasattr(response.headers, 'content-type') and self.content_type_starts_with != None and not response.headers['content-type'].startswith(self.content_type_starts_with):
            return { "url": self.url, "pass": False, "result": f"GET response Content-type header did not start with {self.content_type_starts_with}" }
        if self.text_failure_substr != None and self.text_failure_substr in response.text:
            return { "url": self.url, "pass": False, "result": f"GET response body contained failure substring ||{self.text_failure_substr}||" }
        if self.text_success_substr != None and not self.text_success_substr in response.text:
            return { "url": self.url, "pass": False, "result": f"GET response body did not contain success substring ||{self.text_success_substr}||" }
        
        # If we got this far, it passes
        return { "url": self.url, "pass": True }
