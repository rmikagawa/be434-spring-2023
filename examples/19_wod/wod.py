#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Create WOD
"""


import argparse
import csv
import io
from pprint import pprint
import random
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Create WOD',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='num',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='Input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args
# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    
    with open(fh) as ham:
        reader = csv.DictReader(ham, delimiter=',')
        exercises = []
        for rec in reader:
            name, reps = rec['exercise'], rec['reps']
            reps = reps.split('-')
            low, high = int(reps[0]), int(reps[1]) # what goes here?
            exercises.append((name, low, high))
    
    return exercises

# --------------------------------------------------

def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
def main():
    """Make a jazz noise sdfsdfsdfsdf"""

    args = get_args()
    random.seed(args.seed)

    exercises = read_csv(str(args.file.name))
    exercises_to_do = random.sample(exercises, k=args.num)
    final_ex = []
    for e in exercises_to_do:
        reps = random.randint(e[1], e[2])
        if args.easy == True:
            reps = int(reps/2)
        else:
            reps = reps
        final_ex.append((e[0], reps))
    print(tabulate(final_ex, headers=('Exercise', 'Reps')))

# --------------------------------------------------
if __name__ == '__main__':
    main()
