
diag = []

with open("03A\day03input.txt") as f:
    diag = f.readlines()

targetList = []

for col in diag[0]:
    for row in diag:
        
        onesList = []
        zerosList = []
        
        if row[col:col + 1] == 1:
            onesList.append(row)
        else:
            zerosList.append(row)

    if len(onesList) > len(zerosList):
        targetList = onesList
    else:
        targetList = zerosList

