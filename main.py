import requests
import json
import os

input = os.environ.get('input')
output = os.environ.get('output')
token = os.environ.get('token')
url = os.environ.get('splunk_endpoint')


headers = {'Authorization': 'Splunk ' + os.environ['TOKEN'],
          "Content-Type": "application/json"}

print(input, output, url)
# sarif = json.load(open('test.json',))
# print(len(sarif['event']['runs']))
# for run in sarif['event']['runs']:
#     # print(json.dumps(run))
#     my_data = {"event": run}
#     r = requests.post('https://localhost:8088/services/collector', verify=False,
#                       json=my_data, headers=headers)
#     print(r.status_code, r.text)
