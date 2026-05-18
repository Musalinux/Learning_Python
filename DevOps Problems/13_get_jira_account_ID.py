import requests
from requests.auth import HTTPBasicAuth
import json
import os

url = "https://vasaikarmusaddik.atlassian.net/rest/api/3/myself"

auth = HTTPBasicAuth(
    "vasaikarmusaddik@gmail.com",
    os.getenv("JIRA_API_TOKEN")
)

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=auth)

print(json.dumps(response.json(), indent=4))