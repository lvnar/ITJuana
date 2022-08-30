
from functools import reduce

SIMBOLS = ['X', 'O']

def create_board():
    print('_____________________________________________________________')
    print('TIC - TAC - TOE')
    print('Input your moves in format x,y according to the board...\n')
    return [['' for i in range(3)] for j in range(3)]

def verify_board(board):
    moves = 0

    diagonals = [
        ''.join([board[i][i] for i in range(len(board))]),
        ''.join([board[2-i][i] for i in range(len(board))])
    ]
    
    if 'XXX' in diagonals:
        return 1
    if 'OOO' in diagonals:
        return 2

    for (row, col) in zip(board, zip(*board)):
        r = ''.join(row)
        c = ''.join(col)

        moves += len(r)

        if 'XXX' in [r,c]:
            return 1
        elif 'OOO' in [r,c]:
            return 2
    
    if moves == 9:
        return 3
    return 0

def printBoard(board):
    for r in board:
        print('| ' + ' | '.join([x if x != '' else '_' for x in r]) + ' |')
        
    print('_______________________')

def play(board, player):
    printBoard(board)
    
    move = input('Player {} ({}) next move: '.format(player + 1, SIMBOLS[player]))
    pos = [int(x) for x in move.split(',')]
    
    if len(pos) != 2 or board[pos[0]][pos[1]] != '':
        raise Exception('Invalid move!')
    
    board[pos[0]][pos[1]] = SIMBOLS[player]


playBoard = create_board()
currPlayer = 0
winner = 0

while (winner == 0):
    try:
        play(playBoard, currPlayer)
        winner = verify_board(playBoard)
        currPlayer = (currPlayer + 1) % 2
    except Exception as e:
        print(e, 'Try again...')


printBoard(playBoard)
if winner == 1 or winner == 2:
    print('Player %i is the WINNER!!!' % winner)
else:
    print("No more available moves. It's a tie!")
print('_____________________________________________________________')
