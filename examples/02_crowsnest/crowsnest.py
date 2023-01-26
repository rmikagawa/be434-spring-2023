#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date: January 25, 2023
Purpose: Choose the article.
"""

import argparse
import os
import sys

# --------------------------------------------------

def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    return parser.parse_args()


def main():
    """Pick article based on first character of word"""
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")

if __name__ == '__main__':
    main()
