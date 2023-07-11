#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption
    (CTRL + C), prints those statistics since the beginning: """
import sys


size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0


def print_stats():
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])


try:
    for line in sys.stdin:
        if count == 10:
            print_stats()
            count = 1
        else:
            count += 1

        line = line.split()

        size += int(line[-1])

        try:
            if line[-2] in valid_codes:
                if status_codes.get(line[-2], -1) == -1:
                    status_codes[line[-2]] = 1
                else:
                    status_codes[line[-2]] += 1
        except IndexError:
            pass

    print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
