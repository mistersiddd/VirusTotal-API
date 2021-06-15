import requests
import sys
url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '<your api-key>', 'resource': sys.argv[1]}
response = requests.get(url, params=params)
json_res=response.json()

scans=json_res["scans"]
print(scans)