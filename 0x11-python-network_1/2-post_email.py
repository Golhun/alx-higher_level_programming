#!/usr/bin/python3
"""Sends a POST request with a variable 'email' to a specified URL."""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # Create and send the POST request
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # Read and print the response
        res = response.read()
        print(res.decode('utf-8'))
