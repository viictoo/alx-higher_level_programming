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


def print_status_code():
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
            print_status_code()
            count = 1
        else:
            count += 1

        elements = line.split()

        try:
            size += int(elements[-1])
        except (IndexError, ValueError):
            pass
        try:
            # Get the second-to-last element of `elements` as `status_code`
            status_code = elements[-2]
            if status_code in valid_codes:
                if status_code not in status_codes:
                    # If `status_code` is not in `status_codes`,
                    # add it as a new key with a count of 1
                    status_codes[status_code] = 1
                else:
                    # If `status_code` is already in `status_codes`,
                    # increment its count by 1
                    status_codes[status_code] += 1
        except IndexError:
            # Ignore IndexError if the element doesn't exist
            pass
    print_status_code()

except KeyboardInterrupt:
    print_status_code()
    raise
