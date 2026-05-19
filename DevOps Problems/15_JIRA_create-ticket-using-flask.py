# we just import flask module 
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
import os 

# Create a flask app instance
app = Flask(__name__)

# add a decorator. This performs an action before execution of the function
@app.route("/createJira", methods = ['POST'])

# now define the function 
def createJira ():
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
        "summary": "Ticket created via GitHub Issue"
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
# Flask comes with an inbuilt server, so you dont need to deploy it anywhere

app.run ('0.0.0.0', port=9000)

"""
Since we are unable to expose the IP address directly, we will use ngrok to get a public IP. 
brew install ngrok
ngrok http 9000
"""
