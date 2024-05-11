#!/usr/bin/python3
"""Fetches data from a URL using urllib."""

import urllib.request


def fetch_url_data(url):
    """
    Fetches data from the specified URL.

    Args:
    - url (str): The URL to fetch data from.

    Returns:
    - str: The fetched data.
    """
    with urllib.request.urlopen(url) as response:
        data = response.read()
    return data


def main():
    """Main function to run the script."""
    url = 'https://alx-intranet.hbtn.io/status'
    data = fetch_url_data(url)

    # Print fetched data
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))


if __name__ == "__main__":
    main()
