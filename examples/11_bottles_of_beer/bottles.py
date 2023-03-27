#!/usr/bin/env python3


"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Date   : today
Purpose: Sing bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing bottles of beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of verses',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args
# --------------------------------------------------


def verse(bottle):
    
    bingbong = ''


    if bottle > 2:
        bingbong = f'{bottle} bottles of beer on the wall,\n{bottle} bottles of beer,\nTake one down, pass it around,\n{bottle - 1} bottles of beer on the wall!\n' 
    elif bottle == 2:
        bingbong = f'{bottle} bottles of beer on the wall,\n{bottle} bottles of beer,\nTake one down, pass it around,\n{bottle - 1} bottle of beer on the wall!\n' 
    elif bottle == 1:
        bingbong= f'{bottle} bottle of beer on the wall,\n{bottle} bottle of beer,\nTake one down, pass it around,\nNo more bottles of beer on the wall!'
  
    return bingbong


# --------------------------------------------------

def test_verse():
    """Test verse"""
 
    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])
 
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------


def main():
    """Sing the annoying song"""
    args = get_args()

    bottle = args.num
    
    beets = list(range(bottle, 0, -1))
    
    for i in beets:
        print(verse(i))

    

    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

