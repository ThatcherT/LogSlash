import requests

# read .log file
log_data = []
with open("/var/log/slash/test-slashed.log", "r") as f:
    # each log is separated in a new line
    # append each log to a list
    log_data = ''.join([line.strip() for line in f.readlines()])



host = "prd-p-voxn4"

protocol = "https"
port = 8088
endpoint = "services/collector/raw"
# endpoint = 'services/collector/raw'
url = f"{protocol}://{host}.splunkcloud.com:{port}/{endpoint}"

token = "bc9681db-59fd-445c-9c43-b21e5f23b540"
headers = {"Authorization": f"Splunk {token}"}

r = requests.post(
    url,
    headers=headers,
    json=log_data,
    verify=False,
)
