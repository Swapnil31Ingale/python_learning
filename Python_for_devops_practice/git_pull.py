

import requests

github_pull_details = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(github_pull_details.json()[0]["number"])
