import sys

file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Prints the statistics for file size and status codes."""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code]:
            print("{}: {}".format(status_code, status_codes[status_code]))

try:
    for line in sys.stdin:
        line = line.strip()

        # Parse the line
        try:
            ip, _, _, timestamp, _, request, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)

            # Check that the request is for /projects/260
            if request != 'GET /projects/260 HTTP/1.1':
                continue

            # Increment the status code count
            if status_code in status_codes:
                status_codes[status_code] += 1

            # Add the file size to the total
            file_size += file_size
            line_count += 1

            # Print the statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

        # Skip any lines that do not match the expected format
        except ValueError:
            continue

# Handle keyboard interrupts (CTRL+C)
except KeyboardInterrupt:
    print_statistics()
    raise

print_statistics()
