#!/usr/bin/env python3

"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : March 26, 2023
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    snake = len(seq) - k + 1
    return [] if snake < 1 else [seq[i:i + k] for i in range(snake)]


# --------------------------------------------------
def main():
    """Make happy noises here"""

    args = get_args()

    file1 = args.file1
    file2 = args.file2
    k = args.kmer

    kmers1 = {}
    for line in file1:
        for word in line.split():
            kmer = find_kmers(word, k)
            for i in kmer:
                if i in kmers1:
                    kmers1[i] = kmers1[i] + 1
                else:
                    kmers1[i] = 1

    kmers2 = {}
    for line in file2:
        for word in line.split():
            kmer = find_kmers(word, k)
            for i in kmer:
                if i in kmers2:
                    kmers2[i] = kmers2[i] + 1
                else:
                    kmers2[i] = 1

    for kmer in sorted(set(kmers1) & set(kmers2)):
        print('{:<10} {:>5} {:>5}'.format(kmer, kmers1[kmer], kmers2[kmer]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
