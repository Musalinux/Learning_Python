# GitHub → Jira Integration using Flask, Webhooks & ngrok 🚀

This project demonstrates a simple DevOps automation workflow where a GitHub webhook triggers a Python Flask application, which then creates a Jira ticket automatically using the Jira REST API.

The project was built as part of my DevOps / SRE / Python automation learning journey.

---

# 📌 Workflow

```text
GitHub Issue / Comment
        ↓
GitHub Webhook
        ↓
ngrok Public URL
        ↓
Flask API Endpoint
        ↓
Jira REST API
        ↓
Jira Ticket Created
```

---

# ⚡ Features

- GitHub Webhook Integration
- Flask REST API
- Jira REST API Automation
- Python Requests Library
- Environment Variable based Secret Handling
- ngrok Public Tunnel for Localhost Exposure
- Simple DevOps Automation Example

---

# 🛠️ Technologies Used

- Python
- Flask
- Jira REST API
- GitHub Webhooks
- ngrok
- requests library

---

# 📂 Project Structure

```text
.
├── 15_JIRA_create-ticket-using-flask.py
├── README.md
```

---

# 📜 Flask Application

```python
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
    url = "https://YOUR-DOMAIN.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth(
        "YOUR_EMAIL",
        os.getenv("JIRA_API_TOKEN")
    )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
      "fields": {
        "issuetype": {
          "id": "10003"
        },
        "project": {
          "key": "SCRUM"
        },
        "summary": "Ticket created via GitHub Issue"
      },
      "update": {}
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(
        json.loads(response.text),
        sort_keys=True,
        indent=4,
        separators=(",", ": ")
    )

app.run('0.0.0.0', port=9000)
```

---

# 🔐 Environment Variable Setup

Never hardcode API tokens in source code.

Export the Jira token before running the script:

```bash
export JIRA_API_TOKEN="your_jira_api_token"
```

---

# ▶️ Running the Flask App

```bash
python 15_JIRA_create-ticket-using-flask.py
```

Output:

```text
Running on http://127.0.0.1:9000
Running on http://192.168.x.x:9000
```

---

# 🌍 Exposing Localhost using ngrok

GitHub Webhooks cannot access private/local IP addresses directly.

Install ngrok:

```bash
brew install ngrok
```

Start tunnel:

```bash
ngrok http 9000
```

Example output:

```text
Forwarding https://example.ngrok-free.app -> http://localhost:9000
```

---

# 🔗 GitHub Webhook Configuration

GitHub Repository:

```text
Settings → Webhooks → Add Webhook
```

Payload URL:

```text
https://YOUR-NGROK-URL.ngrok-free.app/createJira
```

Content Type:

```text
application/json
```

Event Trigger:

```text
Issue comments
```

---

# ✅ Result

Whenever the webhook is triggered, a Jira ticket is automatically created in the configured Jira project.

Example created ticket:

```text
SCRUM-7 → Ticket created via GitHub Issue
```

---

# 🧠 What I Learned

- REST APIs
- Flask basics
- GitHub Webhooks
- ngrok tunneling
- Jira automation
- Secret management using environment variables
- DevOps style event-driven automation
- Debugging webhook delivery issues
- HTTP request/response handling

---

# 🚀 Future Improvements

- Create Jira tickets only when a user comments `/createJira`
- Parse GitHub issue title dynamically
- Add Jira description from GitHub issue body
- Add assignee/reporter automatically
- Add Slack notifications
- Deploy Flask app on AWS/GCP
- Add logging & error handling
- Add webhook signature validation

---

# 👨‍💻 Author

Musaddik Vasaikar

GitHub: https://github.com/Musalinux
LinkedIn: https://www.linkedin.com/in/musaddik-vasaikar/
