#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date: April 2, 2023
Purpose: Python program to write a Python program
"""

import argparse
import csv
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='{args.purpose}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default='')

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=str,
                        default="out.csv")

    parser.add_argument('-d',
                        '--delim',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=",")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Filter CSV files"""

    args = get_args()
    fh = args.file.name
    outfile = args.outfile
    col = args.col
    delim = args.delim

    with open(fh) as ham:
        
        reader = csv.DictReader(ham, delimiter=delim)
        fields = reader.fieldnames

        if col != None and col not in fields:
            sys.exit(f'--col "{col}" not a valid column!\n')

        with open(outfile, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fields, extrasaction='ignore', delimiter=delim) # type: ignore
            writer.writeheader()

            rows = 0

            if col != None:
                for rec in reader:
                    if re.search(args.val, rec[col], re.IGNORECASE) != None:
                        rows = rows + 1
                        writer.writerow(rec)
            elif col == None:
                for rec in reader:
                    if re.search(args.val, str(rec), re.IGNORECASE) != None:
                        rows = rows + 1
                        writer.writerow(rec)
    print(f'Done, wrote {rows} to "{str(outfile.name)}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
