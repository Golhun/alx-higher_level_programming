#!/usr/bin/python3
"""
Sends a request to a URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        # Send a request to the specified URL
        with request.urlopen(sys.argv[1]) as res:
            # Display the body of the response
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        # Handle HTTP errors if they occur
        print('Error code:', er.code)
