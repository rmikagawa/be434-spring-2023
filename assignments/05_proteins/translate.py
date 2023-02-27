#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Translate DNA/RNA to proteins
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA into proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A named string argument',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='a writable text file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Translate DNA/RNA to proteins"""

    args = get_args()
    codon_table = {}

    for line in args.codons:
        split = line.rstrip().split()
        codon_table[split[0]] = split[1]

    protein = ""
    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        codon = codon.upper()
        amino_acid = codon_table.get(codon, '-')
        protein += amino_acid

    out_file = args.outfile
    out_file.write(protein)
    print(f'Output written to "{out_file.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
