#!/usr/bin/env python3

"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : April 30, 2023
Purpose: Caesar's cipher
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='A positional argument')

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        default=sys.stdout)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """lalala"""

    args = get_args()
    file = args.positional
    decode = ''

    numbers = {}
    letters = {}
    val = 1

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in alpha:
        numbers[val] = i
        letters[i] = val
        val = val + 1

    new_word = ''
    shift = args.number

    if args.decode is True:
        for line in file:
            for i in line:
                i = i.upper()
                if i not in alpha:
                    decode += i
                elif letters[i] - shift == 0:
                    turnips = 26
                    decode += numbers[turnips]
                elif letters[i] < (shift):
                    turnips = letters[i]
                    decode += numbers[(turnips - shift) + 26]
                else:
                    turnips = letters[i]
                    decode += numbers[turnips - shift]
        decode = decode.rstrip('\n')

    for line in file:
        for i in line:
            i = i.upper()
            if i not in alpha:
                new_word += i
            elif letters[i] < (27 - shift):
                beets = letters[i]
                new_word += numbers[beets + shift]
            else:
                beets = letters[i]
                new_word += numbers[(beets + shift) - 26]

    new_word = new_word.rstrip('\n')

    if args.outfile != sys.stdout:
        with open(args.outfile, 'wt', encoding='utf-8') as output_file:
            if args.decode is True:
                print(decode, file=output_file)
            else:
                print(new_word, file=output_file)
            output_file.close()
    else:
        if args.decode is True:
            print(decode)
        else:
            print(new_word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
