#!/usr/bin/python3
"""Sends a POST request with an 'email' parameter to a specified URL."""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode("ascii")

    # Create and send the POST request
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        # Display the body of the response
        print(response.read().decode("utf-8"))
