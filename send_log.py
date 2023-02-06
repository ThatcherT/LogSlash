# http://http-inputs.prd-p-owj2m.splunkcloud.com:8088/services/collector/event
import requests

host = "prd-p-owj2m"
# host='si-i-03ac3c083b74377d2.prd-p-owj2m'
# host= 'http-inputs-' + host

protocol = "https"
port = 8088
# port=443
endpoint = "services/collector/raw"
# endpoint = 'services/collector/raw'
# url = f"{protocol}://{host}.splunkcloud.com:{port}/{endpoint}"
url = f"http://localhost:8000/article/init"

token = "a9a2a282-c294-4187-a3d2-14377065f449"
headers = {"Authorization": f"Splunk {token}"}

data = {"host": "localhost", "source": "test", "sourcetype": "test", "event": "test"}

for i in range(2):
    r = requests.post(
        url,
        headers=headers,
        json=data,
        verify=False,
    )
print(r)
