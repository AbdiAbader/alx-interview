#!/usr/bin/python3
"""Log Parser"""
import sys


if __name__ == '__main__':
    total_file_size = [0]
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print statistics """
        print('Total file size: {}'.format(total_file_size[0]))
        for status_code in sorted(status_code_counts.keys()):
            count = status_code_counts[status_code]
            if count:
                print('{}: {}'.format(status_code, count))

    def parse_line(line):
        """ Checks the line for matches """
        try:
            line = line[:-1]
            words = line.split(' ')
            # File size is last parameter on stdout
            file_size = int(words[-1])
            total_file_size[0] += file_size
            # Status code comes before file size
            status_code = int(words[-2])
            # Move through dictionary of status codes
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except:
            pass

    line_count = 0
    try:
        for line in sys.stdin:
            parse_line(line)
            line_count += 1
            """ print after every 10 lines """
            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
