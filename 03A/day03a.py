diag = []

with open("03A\day03input.txt") as f:
    diag = f.readlines()

print(len(diag[0]))

i = 0
total = 0
for row in diag:
    total = total + int(row[i:1])



print(result)