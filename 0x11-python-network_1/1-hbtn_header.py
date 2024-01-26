#!/usr/bin/python3
"""takes in a URL, 
sends a request to the URL 
the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request

url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
