import requests
import sys
import json
from config import HCCLinksItem, HCCLinksCollection, HCCLinksConfig
from hcclinks import BaseRequest, HeadRequest, GetRequest

# Read the config from the named file
hccl_config = HCCLinksConfig(sys.argv[1])

# Initialize the list of request objects
hcc_requests = []

# Loop through the collections in the config and build up request objects
for a_collection in hccl_config.collections:
    print(f"Doing collection {a_collection.name}")
    for an_item in a_collection.items:
        if an_item.method == "HEAD":
            hcc_requests.append(HeadRequest(an_item))
        elif an_item.method == "GET":
            hcc_requests.append(GetRequest(an_item))
        else:
            raise ValueError(f"Only HEAD and GET are currently supported, cannot do {an_item.method}!")

# Initialize the list of results objects
hcc_results = []

# Loop through the request objects, firing each and collecting the results
for an_item in hcc_requests:
    hcc_results.append(an_item.check())

# Loop through the results objects, printing each as a JSON string
for a_result in hcc_results:
    print(a_result.as_string(format="json"))