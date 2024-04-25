#!/bin/bash
# Sends a request to a URL and displays the size of the response body in bytes

URL=$1
SIZE=$(curl -sI "$URL" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')
echo "$SIZE"
