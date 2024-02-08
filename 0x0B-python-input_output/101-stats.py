#!/usr/bin/python3

"""
A script to compute metrics based on input from stdin.
"""


import sys

def print_statistics(total_size, status_codes):
    """Print statistics based on total file size and status codes.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing counts of status codes.

    """
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{:d}: {:d}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """Parse a line and update total file size and status code count.

    Args:
        line (str): The input line to parse.
        total_size (int): The current total file size.
        status_codes (dict): A dictionary containing counts of status codes.

    Returns:
        int: The updated total file size.

    """
    parts = line.split()
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    except ValueError:
        pass
    return total_size

def main():
    """Main function to read input, compute statistics, and print them."""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            total_size = parse_line(line.strip(), total_size, status_codes)
            if i % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()
