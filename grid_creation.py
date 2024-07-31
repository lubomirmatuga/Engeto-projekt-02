# GRID CREATOR FUNCTION
def grid_creator(size,empty_sign):
    grid=[]
    for column in range (0,size):
        temp_row=[]
        for row in range(0,size):
            temp_row.append(empty_sign)
        grid.append(temp_row)
    return (grid)