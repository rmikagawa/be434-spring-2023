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


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Substitution cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='SEED',
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

    numbers = {} #holds normal order of alphabet (e.g. 1:A, B:2) with numbers as keys
    letters = {} #holds normal order of alphabet (e.g. A:1, B:2) with letters as keys
    new_code = {} #holds new order of alphabet (e.g. 1:H, 2:K) with numbers as keys
    coded = []
    val = 1

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in alpha: #normal order of alphabet in both letters (e.g. A:1, B:2), and numbers (e.g. 1:A, B:2) as keys
        numbers[val] = i
        letters[i] = val
        val = val + 1

    #random.shuffle(coded) #new randomized order of alphabet
    #print(coded)
    #code_position = 1

    #for i in coded:
    #    new_code[i] = code_position
    #    code_position = code_position + 1

    new_word = ''
    new_alpha = scrambled_eggs(new_code)

    for line in file:
        for i in line:
            i = i.upper()
            if i not in alpha:
               new_word += i
            else:
                new_word += new_alpha[letters[i]] #whatever is the position of letter 'i' --> find the same one in the new_coded dictionary

    #new_word = new_word.rstrip('\n')
    print(new_word)

    #print(''.join([scrambled_eggs(num) for num in nums]))
# --------------------------------------------------
def scrambled_eggs(new_code):
    """Randomly choose a letter"""
    args = get_args()
    random.seed(args.seed)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    alpha_list = []


    for i in alpha:
        alpha_list.append(i)
    
    shuffle(alpha_list)

    new_code = dict(zip(nums, alpha_list))

    return new_code

# --------------------------------------------------
if __name__ == '__main__':
    main()
