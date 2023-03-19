#!/usr/bin/env python3

"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : March 19, 2023
Purpose: Create synthetic sequences
"""

import argparse
import sys
import random


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        nargs='*',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default="out.fa")

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.seqtype not in ['DNA', 'RNA', 'dna', 'rna']:
        parser.error(f'--seqtype "{args.seqtype}" must be DNA or RNA')
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


# --------------------------------------------------

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    num_seq = args.numseqs
    seq_num = 1

    if args.outfile != sys.stdout:
        args.outfile = str(args.outfile)
        args.outfile = str.strip(args.outfile, "'[]'")

    output_file = open(args.outfile, 'wt', encoding='utf-8')

    for i in range(num_seq):
        seq = ""
        seq_len = random.choice(range(args.minlen, args.maxlen))

        for j in range(seq_len):
            seq += random.choice(pool)

        if args.outfile != sys.stdout:
            print(f'>{seq_num}\n{seq}', file=output_file)
        else:
            print(seq)

        seq_num = seq_num + 1
    output_file.close()

    seqtype = args.seqtype
    seqtype = str.upper(seqtype)

    if args.outfile != sys.stdout and num_seq == 1:
        print(f'Done, wrote {num_seq} {args.seqtype} sequence to "{args.outfile}".')
    elif args.outfile != sys.stdout and num_seq > 1:
        print(f'Done, wrote {num_seq} {seqtype} sequences to "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
