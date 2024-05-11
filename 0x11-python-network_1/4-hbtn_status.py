#!/usr/bin/python3
"""
This script fetches the status of https://intranet.hbtn.io/status using the requests library.
"""

import requests

if __name__ == "__main__":
    # Send a GET request to fetch the status
    response = requests.get("https://intranet.hbtn.io/status")

    # Print information about the response
    print("Response Body:")
    print("\t- Response Type: {}".format(type(response.text)))
    print("\t- Response Content: {}".format(response.text))
