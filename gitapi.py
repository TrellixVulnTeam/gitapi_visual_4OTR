#example from PyGithub
from github import Github

# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
g = Github("fa9aff87f25bf654509cabc6748346b685906eed")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
