#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption
    (CTRL + C), prints those statistics since the beginning: """


size = 0
status_codes = {}
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
line_number = 0


def print_status_code():
    """prints stats
    """
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])


if __name__ == "__main__":
    import sys
    try:
        for line in sys.stdin:
            line_number += 1
            if line_number % 10 == 0:
                print_status_code()

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_status_code()

    except KeyboardInterrupt:
        print_status_code()
        raise
