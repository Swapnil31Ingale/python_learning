
def isValidChessBoard(board):
    # Track the count of pieces for each player
    piece_counts = {'b': 0, 'w': 0, 'bpawn': 0, 'wpawn': 0, 'bking' : 0, 'wking' : 0}

    # Valid chess pieces
    valid_pieces = {'bpawn', 'wpawn', 'bknight', 'wknight', 'bbishop', 'wbishop',
                    'brook', 'wrook', 'bqueen', 'wqueen', 'bking', 'wking'}

    # Valid board coordinates
    valid_coordinates = {f'{i}{j}' for i in range(1, 9) for j in 'abcdefgh'}
    #valid_coordinates = set([f'{i}{j}' for i in range(1, 9) for j in 'abcdefgh'])

    for position, piece in board.items():
        # Check if the piece is valid
        if piece not in valid_pieces:
            return False

        # Check if the coordinates are valid
        if position not in valid_coordinates:
            return False

        # Count the pieces for each player
        if piece.startswith('b'):
            piece_counts['b'] += 1
            if piece == 'bpawn':
                piece_counts['bpawn'] += 1
            if piece == 'bking':
                piece_counts['bking'] += 1
        elif piece.startswith('w'):
            piece_counts['w'] += 1
            if piece == 'wpawn':
                piece_counts['wpawn'] += 1
            if piece == 'wking':
                piece_counts['wking'] += 1

    # Check the total counts for each player
    if piece_counts['b'] > 16 or piece_counts['w'] > 16 or piece_counts['bpawn'] > 8 or piece_counts['wpawn'] > 8:
        return False

    # Check if there is exactly one black king and one white king
    if piece_counts['bking'] != 1 or piece_counts['wking'] != 1:
        return False

    return True

# Example usage:
chess_board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess_board))

