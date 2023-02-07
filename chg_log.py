# read ./Vector/logs/one_log.log file
# read in json, add ts, send to splunk

import requests
import json
import time
import os

# read .log file
log_data = []
with open("./Vector/logs/one_log.log", "r") as f:
    # each line has a json object, convert to dict, add key
    for line in f:
        json_obj = line.strip()
        print(json_obj)

