#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Expand IUPAC codes
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """bing bong"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQUENCE',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout,
                        required=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """i hate it here"""

    args = get_args()
    seq = args.seq
    iupac = {'A': 'A', 'C': 'C', 'T': 'T', 'G': 'G', 'U': 'U', 'R': 'AG',
             'Y': 'CT', 'S': 'GC', 'W': 'AT', 'K': 'GT', 'M': 'AC',
             'B': 'CGT', 'D': 'AGT', 'H': 'ACT', 'V': 'ACG', 'N': 'ACGT'}

    final = ''
    size = len(seq)
    for seqs in seq:
        reg = ''
        for i in seqs:
            if i != iupac[i]:
                reg += f'[{iupac[i]}]'
            else:
                reg += iupac[i]
        if seq[size-1] != seqs:
            final += str(seqs + " " + reg + '\n')
        else:
            final += str(seqs + " " + reg)

    if args.outfile != sys.stdout:
        with open(args.outfile.name, 'wt', encoding='utf-8') as output_file:
            print(f'{final}', file=output_file)
            output_file.close()
            print(f'Done, see output in "{args.outfile.name}"')
    else:
        print(final)


# --------------------------------------------------
if __name__ == '__main__':
    main()
