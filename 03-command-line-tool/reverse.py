#To write a command-line tool in Python, you can use the argparse module to parse command-line arguments 
# and the sys module to read input from stdin and write output to stdout.

import argparse
import sys

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Reverse the lines of a file')
    parser.add_argument('filename', help='the file to reverse')
    args = parser.parse_args()

    # Read the input file
    with open(args.filename, 'r') as f:
        lines = f.readlines()

    # Reverse the lines
    lines.reverse()

    # Write the output
    for line in lines:
        sys.stdout.write(line)

if __name__ == '__main__':
    main()
