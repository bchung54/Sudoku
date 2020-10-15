
import time

empty_board = [[0] * 9] * 9

def display(board):
    # Prints out sudoku board with dividers
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:    
            print("---" * 7)                # Separates rows of board with a horizontal divider

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:       
                print("|", end = " ")       # Separates every three columns with a vertical divider
            print(board[i][j], end = " ")   # Displays every number in each row
        
        print()

    return None

def find_empty_cell(board):
    # Takes sudoku board and returns first empty cell
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None


def simple_solve(board):
    empty_cell = find_empty_cell(board)
    if empty_cell:
        row, col = empty_cell
        for i in range(1,10):
            board[row][col] = i
            if validate(board):
                if simple_solve(board):
                    return True
            else:
                board[row][col] = 0

    else:
        print("Done! No empty cells")
        return True

def validate(board):

    # Check all rows for nonzero duplicates
    for row in board:
        row_nonzero = [digit for digit in row if digit != 0]
        if len(row_nonzero) != len(set(row_nonzero)):
            return False
    
    # Check all columns for nonzero duplicates
    for i in range(len(board)):
        column_digits = []
        for j in range(len(board[i])):
            column_digits += [board[j][i]]
        column_nonzero = [digit for digit in column_digits if digit != 0]
        if len(column_nonzero) != len(set(column_nonzero)):
            return False
    
    # Check all boxes for nonzero duplicates
    for box_i in range(2):
        for box_j in range(2):
            box_digits = []
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if i // 3 == box_i and j // 3 == box_j:
                        box_digits += [board[i][j]]
                        box_nonzero = [digit for digit in box_digits if digit != 0]
                        if len(box_nonzero) != len(set(box_nonzero)):
                            return False
    
    return True







easy_board = [
    [2,6,0,0,0,3,0,1,5],
    [4,7,0,0,0,0,0,0,8],
    [5,8,1,0,0,4,7,6,3],
    [0,3,0,4,8,9,0,7,0],
    [0,0,6,0,0,2,8,3,0],
    [0,0,8,3,1,0,0,0,0],
    [6,9,0,0,0,8,0,0,7],
    [3,0,0,0,9,0,2,0,0],
    [0,1,0,5,0,0,0,9,6],
]

med_board = [
    [0,0,0,3,0,0,0,6,2],
    [0,7,3,4,0,0,0,0,0],
    [2,0,0,0,0,0,3,0,0],
    [0,0,0,9,8,0,5,3,1],
    [0,0,1,0,0,7,0,4,9],
    [0,0,0,6,0,0,0,0,0],
    [0,0,6,0,0,0,2,1,8],
    [0,0,4,0,0,6,0,5,0],
    [0,1,7,0,3,2,0,9,0],
]

hard_board = [
    [0,5,0,0,0,0,0,0,0],
    [0,0,3,0,9,0,0,6,2],
    [0,0,0,0,6,0,5,3,8],
    [9,0,0,0,0,1,3,4,0],
    [0,0,0,0,0,0,7,0,0],
    [0,3,0,2,0,0,0,0,0],
    [0,0,0,9,0,5,0,8,0],
    [5,0,0,0,0,7,0,0,0],
    [1,0,9,6,0,0,0,0,4],
]

def solution(board):
    display(board)
    start = time.time()
    simple_solve(board)
    end = time.time()
    print('-' * 10, "Complete: ", end - start, " seconds",'-' * 10)
    display(board)
    return None


solution(hard_board)