#!/usr/bin/env python3

"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : April 30, 2023
Purpose: Substitution cipher
"""

import argparse
import sys
import random
from random import shuffle
import re


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

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
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
    new_code = {}
    letters = {}
    coded = []
    val = 1

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in alpha: #normal order of alphabet in both letters (e.g. A:1, B: 2), and numbers (e.g. 1:A, B:2) as keys
        numbers[val] = i
        letters[i] = val
        val = val + 1

    for i in alpha:
        coded.append(i)

    random.seed(args.seed) 
    random.shuffle(coded) #new randomized order of alphabet
    code_position = 1

    for i in coded:
        new_code[i] = code_position
        code_position = code_position + 1

    new_word = ''
    new_code = {v: k for k, v in new_code.items()}

    for line in file:
        for i in line:
            i = i.upper()
            if i not in alpha:
               new_word += i
            else:
                new_word += new_code[letters[i]] #whatever is the position of letter 'i' --> find the same one in the new_coded dictionary

    new_word = new_word.rstrip('\n')
    print(new_word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
