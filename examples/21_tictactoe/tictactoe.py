#!/usr/bin/env python3
"""
Author : Raine Ikagawa <rikagawa@arizona.edu>
Purpose: Python program to write a Python program
"""


import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command line arguments"""

    parser = argparse.ArgumentParser(
        description='tic tac toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-p',
                        '--player',
                        help='X or O',
                        metavar='player',
                        type=str,
                        default=None)

    parser.add_argument('-b',
                        '--board',
                        help='State of the board',
                        metavar='board',
                        type=str,
                        default='.'*9)

    parser.add_argument('-c',
                        '--cell',
                        help='Choose cell to play in',
                        metavar='CELL',
                        type=int,
                        default=None)

    args = parser.parse_args()
    values = r'XOxo.'
    players = r'XO'

    if args.cell != None:
        if args.cell < 1 or args.cell > 9:
            parser.error(f'--cell {args.cell} must be in 1-9')

    if args.board != '.'*9:
        if len(args.board) > 9 or len(args.board) < 1:
            parser.error(f'--board {args.board} must be 1-9 characters')

    for i in args.board:
        if re.search(values, i) == False:
            parser.error(f'--board {args.board} must contain "X" "O" or "."')

    if args.player != None:
        if args.player not in "XO":
            parser.error(f'--player {args.player} must be "X" or "O"')

    return args


# --------------------------------------------------
def main():
    """boooooop"""

    args = get_args()
    board = args.board
    print (format_board(board))

# --------------------------------------------------
def format_board(board):
    """Format the board"""

    cells = []
    for i, char in enumerate(board, start=1):
        cells.append(str(i) if char == '.' else char)

    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        cells_tmpl.format(cells[0], cells[1], cells[2]), bar,
        cells_tmpl.format(cells[3], cells[4], cells[5]), bar,
        cells_tmpl.format(cells[6], cells[7], cells[8]), bar
    ])
# --------------------------------------------------
def find_winner(board):
    """Determine if there is a winner"""
    return board
# --------------------------------------------------
if __name__ == '__main__':
    main()
