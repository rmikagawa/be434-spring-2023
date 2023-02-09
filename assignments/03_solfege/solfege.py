#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Python program to write a Python program
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        description='to sing about solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('soulfiggy',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""
    args = get_args()
    soulfiggy = args.soulfiggy
    solfege = {'Do': 'A deer, a female deer', 'Re': 'A drop of golden sun',
               'Mi': 'A name I call myself', 'Fa': 'A long long way to run',
               'Sol': 'A needle pulling thread', 'La': 'A note to follow sol',
               'Ti': 'A drink with jam and bread'}
    idk = "I don't know"

    for i in soulfiggy:
        if i in solfege:
            print(f'{i}, {solfege[i]}')
        else:
            print(f'{idk} "{i}"')

# --------------------------------------------------


if __name__ == '__main__':
    main()
