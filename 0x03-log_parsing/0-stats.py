#!/usr/bin/python3
"""Log Parser"""
import sys


if __name__ == '__main__':
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print statistics """
        print('File size: {}'.format(file_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    try:
        for i, line in enumerate(sys.stdin):
            try:
                line = line[:-1]
                word = line.split(' ')
                # File size is last parameter on stdout
                file_size += int(word[-1])
                # Status code comes before file size
                status_code = int(word[-2])
                # Move through dictionary of status codes
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except:
                continue
            """ print after every 10 lines """
            if (i + 1) % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
