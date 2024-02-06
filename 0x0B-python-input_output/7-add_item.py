#!/usr/bin/python3
"""
A module that loads data from json file and saves to another json file
"""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    # Retrieve and load data from file if it exists
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If it doesn't exist, start list with an empty list
    items = []

# Add cmd args to the list
items.extend(sys.argv[1:])

# Update the file
save_to_json_file(items, filename)
