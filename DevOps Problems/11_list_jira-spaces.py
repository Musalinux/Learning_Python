# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://vasaikarmusaddik.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("vasaikarmusaddik@gmail.com", os.getenv("JIRA_API_TOKEN"))


headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads (response.text)

name = output [0]["name"]

print (name)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
