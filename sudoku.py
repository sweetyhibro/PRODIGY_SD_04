def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def is_valid_move(grid, row, col, num):
    # Check if the number is not in the current row
    if num in grid[row]:
        return False
    
    # Check if the number is not in the current column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check if the number is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    row, col = find_empty_location(grid)
    if row is None and col is None:
        return True  # All cells are filled, puzzle is solved
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # Backtrack
            
    return False

# Example Sudoku grid (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Input Sudoku Puzzle:")
print_grid(grid)
print("\nSolving...\n")

if solve_sudoku(grid):
    print("Sudoku Solved:")
    print_grid(grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
