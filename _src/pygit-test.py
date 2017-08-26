from github import Github

g = Github("zoejane", "")

print g
print g.get_user()
print g.get_user().name
print g.get_user().get_repos()

#for repo in g.get_user().get_repos():
#    print repo.name