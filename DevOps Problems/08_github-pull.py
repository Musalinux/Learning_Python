# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

if response.status_code == 200: 
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    for pull in pull_requests: 
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else: 
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
        print ("PR Creators and counts: ")
        for creator, count in pr_creators.items():
            print (f"{creator}: {count} PRs")
else: 
    print ("Wrong API URL provdided")