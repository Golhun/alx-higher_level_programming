#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me and capture the response body.
curl -s -LX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
