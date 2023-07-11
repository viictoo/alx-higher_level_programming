#!/usr/bin/python3
"""load add save module
    script that adds all arguments to a Python list,
    and then save them to a file:
"""
from sys import argv as av


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    content = load_from_json_file(file)

except FileNotFoundError:
    content = []

content.extend(av[1:])
save_to_json_file(content, file)
