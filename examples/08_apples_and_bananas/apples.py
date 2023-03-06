#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: do the apples and baneenees
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='{args.purpose}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='The string to change banana')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args
    

# --------------------------------------------------
def main():
    """Translate vowels"""

    args = get_args()
    text = args.text
    v=args.vowel
    new = ''

    for char in text:
        if char in 'aeiou':
            new += v
        elif char in "AEIOU":
            new+= v.upper()
        else:
            new += char
    print(new)

    #if file:
    #    print('yarrrr')


# --------------------------------------------------
if __name__ == '__main__':
    main()
