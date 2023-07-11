#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption
    (CTRL + C), prints those statistics since the beginning: """
import sys


size = 0
status_codes = {}
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_number = 0

try:
    for line in sys.stdin:
        line_number += 1
        if line_number == 10:
            print("File size:", size)
            for key in sorted(status_codes):
                print(key + ":", status_codes[key])
            line_number = 0

        elements = line.split()

        try:
            size += int(elements[-1])
        except (IndexError, ValueError):
            pass

        try:
            status_code = elements[-2]
            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(status_code,
                                                             0) + 1
        except IndexError:
            pass

    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])

except KeyboardInterrupt:
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])
    raise
