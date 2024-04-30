#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print("Body response:")
            print("\t- type:", type(data))
            print("\t- content:", data)
            print("\t- utf8 content:", data.decode('utf-8'))
    except Exception as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
