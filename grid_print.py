# GRID PRINTER FUNCTION
def grid_printer(grid):
    size = len(grid)
    print(" ", end=" ")
    for row in range (0, size):
        row+=1
        print(row,end= " ")
    print()
    for i in range (0,size):
        print(i+1, end=" ")
        for j in range (0, size):
            print(grid[i][j], end=" ")
        print()