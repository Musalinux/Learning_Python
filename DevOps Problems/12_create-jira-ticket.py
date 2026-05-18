import requests
from requests.auth import HTTPBasicAuth
import json
import os 

url = "https://vasaikarmusaddik.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("vasaikarmusaddik@gmail.com", os.getenv("JIRA_API_TOKEN"))

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "issuetype": {
      "id": "10003"
    },
    "project": {
      "key": "SCRUM"
    },
    "reporter": {
      "id": "61b613280f02490069c7bb05"
    },
    "summary": "Musa second Jira ticket"
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))