diag = []

with open("03A\day03input.txt") as f:
    diag = f.readlines()

i = 0
gamma = ""
epsilon = ""

# So, like, we look at the data like a grid, and we're basically counting the 1s and 0s in each column of the grid.

# The while loop loops through each column. Inside that, the for loop goes through each row and slices the column we need.
# Then we just total up the numbers of each column in integer, so we can compare it to half the length of the column.

# If the number of 1s is greater than half of all the rows, it's the most common, and we'll mark a "1" for that column.
# If not, we'll mark a "0" for that column.

# To calculate epsilon, it's just the inverse of gamma, so we just flip the comparison.

while i < (len(diag[0]) - 1):
    
    columnTotal = 0
    for row in diag:
        columnTotal = columnTotal + int(row[i:i + 1])
    
    if columnTotal > (len(diag) / 2):
        gamma += "1"
    else:
        gamma += "0"

    if columnTotal < (len(diag) / 2):
        epsilon += "1"
    else:
        epsilon += "0"
    
    i += 1

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)
