#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Find common words
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout,
                        required=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Do something"""

    args = get_args()
    words1 = set()
    words2 = set()

    for line in args.FILE1:
        for word in line.split():
            words1.add(word)

    for line in args.FILE2:
        for word in line.split():
            words2.add(word)

    same = words1.intersection(words2)

    if args.outfile != sys.stdout:
        with open(args.outfile.name, 'wt', encoding='utf-8') as output_file:
            for i in same:
                print(i, file=output_file)
            output_file.close()
    else:
        for i in same:
            print(i)


# --------------------------------------------------
if __name__ == '__main__':
    main()
