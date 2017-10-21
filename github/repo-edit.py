# A simple github interaction script for editing your repos
# `pip install pygithub`
# You'll need to set GH_TOKEN and GH_USER environment variables
# You can make your token here: https://github.com/settings/tokens

from github import Github
import argparse, os, sys

access_token = os.environ['GH_TOKEN']
username = os.environ['GH_USER']

p = argparse.ArgumentParser()

p.add_argument("--issues", help="Issues can be True or False", type = lambda s : s, choices=["True", "true", "False", "false"])
p.add_argument("--wiki", help="Wiki can be True or False", type = lambda s : s, choices=["True", "true", "False", "false"])
p.add_argument("--repository", help="Which repository?", type = lambda s : s)

gh = Github(username, access_token)

args = p.parse_args()

repolist = [r.name for r in gh.get_user().get_repos()]
print("The list of repositories is:",repolist)

print("args is: ", args)

if args.repository in repolist:
	repo = gh.get_user().get_repo(args.repository)
	print("Your repo: ", args.repository, " is real!")

	if args.issues == 'true':
		repo.edit(has_issues=True)
		print("Issues turned on")
	elif args.issues == 'false':
		repo.edit(has_issues=False)
		print("Issues turned off")
	if args.wiki == 'true':
		repo.edit(has_wiki=True)
		print("Wiki turned on")
	elif args.wiki == 'false':
		repo.edit(has_wiki=False)
		print("Wiki turned off")
