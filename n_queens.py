def is_safe(board, row, col, n):
    # Check if no queens can attack the current cell

    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    # Base case: All queens are placed
    if row == n:
        for i in range(n):
            print(" ".join(["Q" if x == 1 else "." for x in board[i]]))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n)
            board[row][col] = 0  # Backtrack

if __name__ == "__main__":
    n = int(input("Enter the board size (N): "))
    first_queen_row = int(input("Enter the row (0-based) for the first queen: "))
    first_queen_col = int(input("Enter the column (0-based) for the first queen: "))

    board = [[0 for _ in range(n)] for _ in range(n)]
    board[first_queen_row][first_queen_col] = 1  # Place the first queen

    if n < 4:
        print("No solution exists for N < 4.")
    else:
        solve_n_queens(board, 1, n)
