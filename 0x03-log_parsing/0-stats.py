#!/usr/bin/python3
"""Log Parser"""
import sys
import re
from collections import defaultdict


def print_stats(file_size, status_codes):
    """ Print statistics """
    print(f"File size: {file_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print(f"{key}: {status_codes[key]}")


if __name__ == '__main__':
    file_size = 0
    status_codes = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            match = re.match(r'^.* (\d+) (\d+)$', line)
            if not match:
                continue
            status_code, size = match.groups()
            status_code = int(status_code)
            size = int(size)
            file_size += size
            status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)
