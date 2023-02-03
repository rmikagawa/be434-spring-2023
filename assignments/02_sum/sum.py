#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Add numbers
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('INT',
                        help='Numbers to add',
                        nargs='+',
                        metavar='INT',
                        type=int,
                        default=0)
    return parser.parse_args()

# --------------------------------------------------


def main():
    """Sum some stuff"""
    args = get_args()
    ints = args.INT
    sum_ints = sum(ints)
    length = len(ints)
    sum_str = str(sum_ints)
    ints_str = [str(x) for x in ints]

    if length == 1:
        print(f'{ints[0]} = {ints[0]}')
    else:
        statement = ' + '.join(ints_str)
        print(f'{statement} = {sum_str}')
# --------------------------------------------------


if __name__ == '__main__':
    main()
