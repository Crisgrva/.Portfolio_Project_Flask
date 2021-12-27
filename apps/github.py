import requests
import time
import json
from os.path import exists

username = "crisgrva"
URLINFO = f"https://api.github.com/users/{username}"
URLREPO = f"https://api.github.com/users/{username}/repos"
localtime = time.localtime().tm_min

if localtime % 5 == 0 or not exists("info.json"):
    info = requests.get(URLINFO).json()
    repos = requests.get(URLREPO).json()
    print("-----------------")
    print("Hice una petición")
    print("-----------------")
    with open("info.json", mode="w", encoding="utf-8") as infoFile:
        json.dump(info, infoFile)

    with open("repos.json", mode="w", encoding="utf-8") as infoFile:
        json.dump(repos, infoFile)
else:
    with open("info.json", "r", encoding="utf-8") as f:
        info = json.loads(f.read())

    with open("repos.json", "r", encoding="utf-8") as f:
        repos = json.loads(f.read())


class Project():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


projects = [Project(**project) for project in repos]

DataPackage = [projects, {
    "username": info['login'],
    "name": info['name'],
    "public_repos": info['public_repos'],
    "avatar_url": info['avatar_url'],
    "biography": info['bio'],
    "twitter": info['twitter_username'],
    "cover": f"https://raw.githubusercontent.com/{username}/{username}/main/Cover.png"
}]
