#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Emulate wc (word count)
"""

import argparse
import os
import sys

# --------------------------------------------------

def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*', #will turn this into list
                        type=argparse.FileType('r'),
                        help='Input file(s)',
                        default=sys.stdin)

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Unknown"""
#print('{:0.02f}'.format(path.pi))
#print(f'{math.pi:0.02f}')
#print(f'{num_lines:8}') (formats in a field 8 characters wide)
#idea is that line, words, characters will be 8 char wide
#followed by a " " then the file name
    args = get_args()


    num_lines = 0
    num_words = 0
    num_char = 0
    total_lines, total_words, total_char = 0,0,0

    for fh in args.file:
        for line in fh:
            num_lines += 1
            num_char += len(line)
            num_words += len(line.split())

        total_lines += num_lines
        total_char += num_char
        total_words += num_words

        print(f'{num_lines:8}{num_words:8}{num_char:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_char:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
