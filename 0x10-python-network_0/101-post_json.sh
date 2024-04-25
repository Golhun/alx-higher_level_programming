#!/bin/bash
# Send a JSON POST request to a URL and display the body of the response.
if ! jq . "$2" &>/dev/null; then echo "Not a valid JSON"; exit 1; fi
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
