import requests
import json

# Set up variables
repo_owner = christian-discovery
repo_name = test
workflow_name = run_work.yml
personal_access_token = secret.token
event_type = "push"
ref = "refs/heads/main"

# Set up the request URL
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches"

# Set up the request headers
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {personal_access_token}"
}

# Set up the request payload
payload = {
    "ref": ref,
    "inputs": {
        "event_type": event_type
    }
}

# Send the POST request to trigger the workflow
response = requests.post(url, headers=headers, json=payload)

# Print the response status code and message
print(f"Response: {response.status_code} {response.reason}")
