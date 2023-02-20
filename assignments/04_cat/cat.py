#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Homework submission
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='a boolean flag',
                        action='store_true')

    args = parser.parse_args()

    return args

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    line_num = 0

    for file_handle in args.file:
        line_num = 0
        for line in file_handle:
            if args.number:
                line_num = line_num + 1
                sys.stdout.write(f'{str(line_num).rjust(6)}\t{line}')
            else:
                sys.stdout.write(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
