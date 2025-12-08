import json
from pathlib import Path
from pprint import pprint

__all__ = [ "HCCLinksItem", "HCCLinksCollection", "HCCLinksConfig" ]

class HCCLinksItem:
    def __init__(self, item_obj):
        self.url = item_obj['url']
        self.description = item_obj['description']
        if 'comment' in item_obj:
            self.comment = item_obj['comment']
        if 'method' in item_obj:
            self.method = item_obj['method']
        else:
            self.method = 'HEAD'
        if 'minStatus' in item_obj:
            self.min_status = item_obj['minStatus']
        else:
            self.min_status = 200
        if 'maxStatus' in item_obj:
            self.max_status = item_obj['maxStatus']
        else:
            self.max_status = 399
        if 'textSuccessSubstr' in item_obj:
            self.text_success_substr = item_obj['textSuccessSubstr']
        if 'textFailureSubstr' in item_obj:
            self.text_failure_substr = item_obj['textFailureSubstr']
        if 'locationHeaderSubstr' in item_obj:
            self.location_header_substr = item_obj['locationHeaderSubstr']
        if 'contentTypeStartsWith' in item_obj:
            self.content_type_starts_with = item_obj['contentTypeStartsWith']
    
    def __str__(self):
        return f"HCCLinksItem:Medhod={self.method}"

class HCCLinksCollection:
    def __init__(self, collection_obj):
        self.items = []
        self.name = collection_obj['name']
        for file_item in collection_obj['items']:
            self.items.append(HCCLinksItem(file_item))
            print(f"Last item in ||{str(self)}|| is ||{str(self.items[-1])}||")
    
    def __str__(self):
        return f"HCCLinksCollection:Items={len(self.items)}"

class HCCLinksConfig:
    def __init__(self, pathname):
        self.collections = []
        conf_path = Path(pathname)
        with conf_path.open() as conf_file:
            self.conf_obj = json.load(conf_file)
        self.description = self.conf_obj['description']
        self.source_bundle_id = self.conf_obj['sourceBundleId']
        for file_collection in self.conf_obj['collections']:
            self.collections.append(HCCLinksCollection(file_collection))

    def __str__(self):
        return f"HCCLinksConfig:Collections={len(self.collections)},Description={self.description}"