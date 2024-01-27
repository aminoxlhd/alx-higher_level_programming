#!/usr/bin/python3
""" takes in a URL, sends a request to the URL """

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
