import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print (response.json())