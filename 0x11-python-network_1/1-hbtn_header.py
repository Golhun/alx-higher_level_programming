#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

def get_x_request_id(url):
    """
    Sends a request to the specified URL and retrieves the value of X-Request-Id.

    Args:
    - url (str): The URL to send the request to.

    Returns:
    - str or None: The value of X-Request-Id if available, otherwise None.
    """
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            return dict(response.headers).get("X-Request-Id")
    except Exception as e:
        print(f"Error fetching X-Request-Id: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id not found.")
