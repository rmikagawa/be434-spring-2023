#!/usr/bin/env python3

"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : April 16, 2023
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    if os.path.exists(args.positional) is True:
        with open(args.positional, 'r', encoding='utf-8') as file:
            dna = file.read()
    elif isinstance(args.positional, str) is True:
        dna = args.positional
    else:
        parser.error("Must provide string or file directory")

    return dna


# --------------------------------------------------
def main():
    """jazz"""

    dna = get_args()

    print(condense(dna))


# --------------------------------------------------
def condense(dna):
    "Create RLE"

    nuc = dna[0]
    nuc_num = 1
    rle = [nuc]

    for i in dna[1:]:
        if i == nuc:
            nuc_num = nuc_num + 1
        elif i != nuc and nuc_num == 1:
            nuc = i
            rle.append(nuc)
        elif i != nuc and nuc_num > 1:
            rle.extend((str(nuc_num), i))
            nuc = i
            nuc_num = 1
        elif i != nuc and nuc_num == 1:
            rle.append(nuc)

    if nuc_num > 1:
        rle.append(str(nuc_num))

    rle = ''.join(rle)
    return rle


# --------------------------------------------------
if __name__ == '__main__':
    main()
