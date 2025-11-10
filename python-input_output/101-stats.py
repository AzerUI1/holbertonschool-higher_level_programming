#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

After every 10 lines or a keyboard interruption (CTRL + C),
it prints:
- Total file size
- Number of lines by status code (sorted by status code)
"""

import sys


def print_stats(total_size, status_codes):
    """Prints the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) >= 2:
                # Try to parse file size
                try:
                    size = int(parts[-1])
                    total_size += size
                except (ValueError, IndexError):
                    pass

                # Try to parse status code
                if parts[-2] in valid_codes:
                    code = parts[-2]
                    status_codes[code] = status_codes.get(code, 0) + 1

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
