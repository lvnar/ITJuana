# Chess Rock movement
#You have a chessboard with only the Rook on it. The Rook can move up, 
# down, left or right from your perspective. Write a function (or a class) 
# that takes a series of movements and at the  end of the sequence of 
# movements prints two numbers: 
# a. The distance traveled by the Rook 
# b. How far away the Rook is from its starting point 
# Assume that the chessboard has no edges (the rook can travel any distance in any direction) 


def create_moves(moves):
    for move in moves:
        move = move.split()
        
        if move[0] in ['up', 'down']:
            dir = 'vertical'
        elif move[0] in ['right', 'left']:
            dir = 'horizontal'
        else:
            raise Exception('Invalid movement!')
        steps = int(move[1])

        if move[0] in ['down', 'left']:
            steps *= -1
        
        yield {
            'direction': dir,
            'steps': steps
        }


def chessBoard(movements):
    moves = create_moves(movements)

    total_steps = 0
    position = {
        'vertical': 0,
        'horizontal': 0
    }

    for move in moves:
        position[move['direction']] += move['steps']
        total_steps += abs(move['steps'])
    
    print('Total steps:', total_steps)
    print('Distance:', abs(position['vertical']) + abs(position['horizontal']))


# Example:
# If the Rook is moved in the following sequence (up 1, left 3, down 2), 
# then the Rook as traveled a distance of 6 spaces, and is 4 spaces away from its starting point
chessBoard(('up 1', 'left 3', 'down 2'))
