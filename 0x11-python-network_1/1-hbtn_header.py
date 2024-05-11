#!/usr/bin/python3
"""Script sends a request and displays the value of X-request-id."""


import urllib.request
import sys

def get_request_id(url):
    """
    Sends a request to the specified URL and retrieves the value of X-Request-Id.

    Args:
    - url (str): The URL to send the request to.

    Returns:
    - str or None: The value of X-Request-Id if available, otherwise None.
    """
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            return headers.get('X-Request-Id')
    except Exception as e:
        print(f"Error fetching X-Request-Id: {e}")
        return None

def main():
    """Main function to run the script."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)

    if request_id:
        print("X-Request-Id:", request_id)
    else:
        print("X-Request-Id not found.")

if __name__ == '__main__':
    main()
