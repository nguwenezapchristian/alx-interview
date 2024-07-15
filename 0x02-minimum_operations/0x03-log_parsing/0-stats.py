#!/usr/bin/python3
import sys
import signal
"""
0-stats.py
Prints statistics about Nginx logs stored in a file passed as an argument.
"""


""" Initialize metrics """
total_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
valid_status_codes = set(status_codes_count.keys())
line_count = 0


def print_stats():
    """ Print the computed metrics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """ Handle the keyboard interruption signal """
    print_stats()
    sys.exit(0)


""" Register the signal handler """
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        """Extract status code and file size"""
        status_code = parts[-2]
        file_size = parts[-1]

        """ Update metrics if the line is valid"""
        if status_code in valid_status_codes:
            status_codes_count[status_code] += 1

        try:
            total_size += int(file_size)
        except ValueError:
            pass

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass
finally:
    print_stats()
