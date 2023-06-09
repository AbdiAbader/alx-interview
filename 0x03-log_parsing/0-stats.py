#!/usr/bin/python3

"""Log Parser"""

import sys


if __name__ == '__main__':
    total_file_size = [0]
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}

    def print_statistics():
        """ Print statistics """
        print('Total file size: {}'.format(total_file_size[0]))
        for status_code in sorted(status_code_counts.keys()):
            if status_code_counts[status_code]:
                print('{}: {}'.format(status_code, status_code_counts[status_code]))

    def parse_line(line):
        """ Checks the line for matches """
        try:
            line = line[:-1]
            words = line.split(' ')
            # File size is last parameter on stdout
            total_file_size[0] += int(words[-1])
            # Status code comes before file size
            status_code = int(words[-2])
            # Move through dictionary of status codes
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except BaseException:
            pass

    line_number = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """ print after every 10 lines """
            if line_number % 10 == 0:
                print_statistics()
            line_number += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
    print_statistics()
