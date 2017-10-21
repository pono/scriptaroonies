# A simple github interaction script for editing your repos
# `pip install pygithub`
# You'll need to set GH_TOKEN and GH_USER environment variables
# You can make your token here: https://github.com/settings/tokens

from github import Github
import argparse, os, sys

access_token = os.environ['GH_TOKEN']
username = os.environ['GH_USER']

p = argparse.ArgumentParser()

p.add_argument("--issues", help="Issues can be True or False")
p.add_argument("--repository", help="Which repository?")
p.add_argument("--wiki", help="Wiki can be True or False")


gh = Github(username, access_token)

args = p.parse_args()

notlist = [r.name for r in gh.get_user().get_repos()]
print("The list of repositories is:",notlist)

if args.repository in notlist:
	repo = gh.get_user().get_repo(args.repository)
	print("Your repo: ", args.repository, " is real!")

	if args.issues == 'True':
		repo.edit(has_issues=True)
		print("Issues turned on")
	elif args.issues == 'False':
		repo.edit(has_issues=False)
		print("Issues turned off")
	if args.wiki == 'True':
		repo.edit(has_wiki=True)
		print("Wiki turned on")
	elif args.wiki == 'False':
		repo.edit(has_wiki=False)
		print("Wiki turned off")
