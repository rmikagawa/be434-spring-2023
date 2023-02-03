#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : 2023-01-26
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Greetings and salutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        action='store_true')

    return parser.parse_args()


def main():
    """Assemble the greeting"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = "." if args.excited is False else "!"

    print(f"{greeting}, {name}{excited}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
