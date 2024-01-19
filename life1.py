import copy

def gameOfLife(board):
    neighborhood = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    arrlen = len(board[0])
    boardlen = len(board)
    board_copy = copy.deepcopy(board)
    for index1, arr in enumerate(board):
        for index2, element in enumerate(arr):
            live = 0
            dead = 0
            for neighbour in neighborhood:
                if 0 <= (index1 + neighbour[0]) < boardlen and 0 <= (index2 + neighbour[1]) < arrlen:
                    if board_copy[index1 + neighbour[0]][index2 + neighbour[1]] == 1:
                        live += 1
                    else:
                        dead += 1
            if board_copy[index1][index2] == 1 and live < 2:
                board[index1][index2] = 0
            elif board_copy[index1][index2] == 1 and live == 2 or live == 3:
                board[index1][index2] = 1
            elif board_copy[index1][index2] == 1 and live > 3:
                board[index1][index2] = 0
            elif board_copy[index1][index2] == 0 and live == 3:
                board[index1][index2] = 1
    return board


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board1 =  [[1,1],[1,0]]
    print(gameOfLife(board))