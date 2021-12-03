import operator

diag = []

with open("03A\day03input.txt") as f:
    diag = f.readlines()

i = 0
gamma = ""
epsilon = ""
while i < (int(len(diag[0])) - 1):
    
    columnTotal = 0
    for row in diag:
        columnTotal = columnTotal + int(row[i:i + 1])
    
    if columnTotal > (int(len(diag)) / 2):
        gamma += "1"
    else:
        gamma += "0"

    if columnTotal < (int(len(diag)) / 2):
        epsilon += "1"
    else:
        epsilon += "0"
    
    i += 1

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma * epsilon)
