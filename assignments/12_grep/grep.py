#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Python program to write a Python program
"""


import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('PATTERN',
                        type=str,
                        help='Search pattern')
    
    parser.add_argument('FILE',
                        type=argparse.FileType('rt', encoding='utf-8'),
                        nargs='*',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt', encoding='utf-8'),
                        default=sys.stdout)


    parser.add_argument('-i',
                        '--insensitive',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    boop = []

    pattern = args.PATTERN

    if len(args.FILE) > 1:
        for i in args.FILE:
            with open(i.name) as file:
                for line in file:
                    if args.insensitive != False:
                        if re.search(pattern, line, re.IGNORECASE) != None:
                            boop.append(line)
                    elif re.search(pattern, line) != None:
                            boop.append(line)
                    else:
                        continue
    elif len(args.FILE) == 1:
        for i in args.FILE:
            with open(i.name) as file:
                for line in file:
                    if args.insensitive != False:
                        if re.search(pattern, line, re.IGNORECASE) != None:
                            boop.append(line)
                    elif re.search(pattern, line) != None:
                        boop.append(line)
                    else:
                        continue

    if args.outfile != sys.stdout:
        with open(args.outfile.name, 'wt', encoding='utf-8') as output_file:
            for i in boop:
                print(i, file=output_file)
            output_file.close()
    else:
        for i in boop:
            sys.stdout.write(i)


# --------------------------------------------------
if __name__ == '__main__':
    main()
