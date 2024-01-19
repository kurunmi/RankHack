import copy
def gameOfLife(board):
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board_copy = copy.deepcopy(board)
    board_len = len(board)
    array_len = len(board[0])
    for index, arr in enumerate(board):
        for inner_index, value in enumerate(arr):
            live = 0
            dead = 0
            for ne in neighbor_offsets:
                x = index + ne[0]
                y = inner_index + ne[1]
                if 0 <= x < board_len and 0 <= y < array_len:
                    if board_copy[x][y] == 1:
                        live += 1
                    else:
                        dead += 1
            if board_copy[index][inner_index] == 1 and live < 2 or live > 3:
                board[index][inner_index] = 0
            elif board_copy[index][inner_index] == 1 and live == 2 or live == 3:
                board[index][inner_index] = 1
            elif board_copy[index][inner_index] == 0 and live == 3:
                board[index][inner_index] = 1
    return board


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board1 =  [[1,1],[1,0]]
    print(gameOfLife(board1))



