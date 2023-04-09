#!/usr/bin/env python3

"""
Author : Raine <rikagawa>
Date   : {today}
Purpose: Password maker
"""

import argparse
import random
import re


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Minimum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)


    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()
# --------------------------------------------------
def clean(word):
    """Remove non-letters from word"""
    word = re.sub(r'[^\w\s]', '', word)
    return word

# --------------------------------------------------
def ransom():
    pass

# --------------------------------------------------

def l33t():
    pass

# --------------------------------------------------
def test_clean():
    """Test clean"""

    assert clean('') == ''
    assert clean('states,') == 'states'
    assert clean("Don't") == 'Dont'
# --------------------------------------------------
def main():
    """password maker"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len


    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                
                    words.add(word)
    words = sorted(words)
    print(''.join(random.sample(words, k=args.num_words)))
# --------------------------------------------------
if __name__ == '__main__':
    main()
