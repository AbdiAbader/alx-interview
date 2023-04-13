#!/usr/bin/python3
import sys

def compute_stats(lines):
    # Initialize variables
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    # Process each line
    for i, line in enumerate(lines):
        # Parse the line
        try:
            _, _, _, _, _, request, status, size, _ = line.split()
            if request != 'GET /projects/260 HTTP/1.1':
                continue
            size = int(size)
            status = int(status)
        except ValueError:
            # Skip lines that don't match the format
            continue

        # Update metrics
        total_size += size
        if status in status_counts:
            status_counts[status] += 1

        # Print stats every 10 lines or at end of input
        if (i + 1) % 10 == 0 or i == len(lines) - 1:
            print(f'Total file size: {total_size}')
            for status_code in sorted(status_counts.keys()):
                if status_counts[status_code]:
                    print(f'{status_code}: {status_counts[status_code]}')

if __name__ == '__main__':
    lines = []
    try:
        # Read input from stdin
        for line in sys.stdin:
            lines.append(line.strip())

            # Process lines every 10 lines
            if len(lines) == 10:
                compute_stats(lines)
                lines = []

        # Process any remaining lines
        if len(lines) > 0:
            compute_stats(lines)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL+C)
        if len(lines) > 0:
            compute_stats(lines)
        raise