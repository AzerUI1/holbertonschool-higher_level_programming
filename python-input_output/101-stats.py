#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
After every 10 lines or when interrupted (CTRL + C),
prints the total file size and number of lines by status code.
"""

import sys

if __name__ == "__main__":
    total_size = 0
    status_counts = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 9:
                # Extract status code and file size safely
                try:
                    status = int(parts[-2])
                    size = int(parts[-1])
                    total_size += size
                    if status in valid_codes:
                        status_counts[status] = status_counts.get(status, 0) + 1
                except (ValueError, IndexError):
                    pass

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_counts):
                    print("{}: {}".format(code, status_counts[code]))

    except KeyboardInterrupt:
        # Print final stats before exiting
        print("File size: {}".format(total_size))
        for code in sorted(status_counts):
            print("{}: {}".format(code, status_counts[code]))
        raise

    # Final stats after all lines processed
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))
