#!/usr/bin/python3

def isSudoku(board):
    board_data = []
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            if value != '.':
                board_data.append((i, value))
                board_data.append((value, j))
                board_data.append((i//3, j//3, value))
    return len(board_data) == len(set(board_data))

if __name__ == '__main__':
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            ,["6", ".", ".", "1", "9", "5", ".", ".", "."]
            ,[".", "9", "8", ".", ".", ".", ".", "6", "."]
            ,["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            ,["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            ,["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            ,[".", "6", ".", ".", ".", ".", "2", "8", "."]
            ,[".", ".", ".", "4", "1", "9", ".", ".", "5"]
            ,[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(isSudoku(board))



