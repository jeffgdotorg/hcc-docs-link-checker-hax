import json
from inspect import ismethod
__all__ = [ "HCCLinkCheckResult" ]

def get_attr_unless_none(source_obj, attr_name):
    if getattr(source_obj, attr_name, None) != None:
        return getattr(source_obj, attr_name)

class HCCLinkCheckResult(object):
    def __init__(
        self,
        hccl_item=None,
        passes=None,
        status=None,
        reason=None,
        content_type=None,
        location_header=None
    ):
        if hccl_item is not None:
            self.description = get_attr_unless_none(hccl_item, "description")
            self.comment = get_attr_unless_none(hccl_item, "comment")
            self.url = get_attr_unless_none(hccl_item, "url")
            self.method = get_attr_unless_none(hccl_item, "method")
            self.min_status = get_attr_unless_none(hccl_item, "min_status")
            self.max_status = get_attr_unless_none(hccl_item, "max_status")
            self.text_success_substr = get_attr_unless_none(hccl_item, "text_success_substr")
            self.text_failure_substr = get_attr_unless_none(hccl_item, "text_failure_substr")
            self.location_header_substr = get_attr_unless_none(hccl_item, "location_header_substr")
            self.content_type_starts_with = get_attr_unless_none(hccl_item, "content_type_starts_with")
        self.pases = passes
        self.status = status
        self.reason = reason
        self.content_type = content_type
        self.location_header = location_header

    def as_string(self, attrs=None, format="json"):
        proxy_dict = dict()
        if attrs is None:
            for an_attr in [name for name in dir(self) if name[0] != '_' and name != 'hccl_item']:
                if not ismethod(getattr(self, an_attr)):
                    proxy_dict[an_attr] = getattr(self, an_attr, None)
        else:
            for an_attr in attrs:
                if not ismethod(getattr(self, an_attr)):
                    proxy_dict[an_attr] = getattr(self, an_attr, None)
        if format != "json":
            raise ValueError(f"Only JSON format is currently supported. I know nothing about the requested format '{format}'.")
        return json.dumps(proxy_dict, sort_keys=True, indent=4)