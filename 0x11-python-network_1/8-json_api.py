#!/usr/bin/python3
"""  takes in a letter and sends a POST request """


import sys
import requests


if __name__ == "__main__":
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    pa = {"q": let}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pa)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
