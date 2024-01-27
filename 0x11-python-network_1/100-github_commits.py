#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge """


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    req = requests.get(url)
    com = req.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                com[a].get("sha"),
                com[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
