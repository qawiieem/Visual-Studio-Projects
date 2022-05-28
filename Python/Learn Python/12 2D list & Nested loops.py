num_grid = [
    [1,2,3],
    [4,5,6],                   #4rows & 3 collumns
    [7,8,9],
    [0]
]

print(num_grid[2]  [1])
#             [row][column]               row = horizontal , collumn = vertical

print(" ")

for row in num_grid:                  #nested for loops
    for col in row:
        print(col)

