sudoku_board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ]


def print_board(board):        # prints out the board in a more legible format

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


def is_cell_empty(board):     # finds the empty spaces (marked 0) on the sudoku board

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None


def valid(board, pos, num):         # returns true if the attempted move is valid

    # Check row
    for i in range(0, 9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(0, 9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):       # inputs a value into empty spaces starting with 1 using backtracking

    empty = is_cell_empty(board)
    if empty:
        row, col = empty
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0     # undo the current cell for backtracking

    return False

print_board(sudoku_board)       # unsolved board
print("\n")
if solve(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution")