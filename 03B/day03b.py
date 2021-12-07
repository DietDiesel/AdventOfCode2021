with open("03A\day03input.txt") as f:
    diag = f.readlines()

for row in diag: # Trim off the line break character at the end of each row
    row = row[0:12]

onesList = diag
zerosList = diag
col = 0

while col < (len(diag[0]) - 1):

    oxygenList = [] # Reset the target lists to be ready to received sorted rows
    scrubberList = []

    for row in diag: # First, add up all the ones in a column to facilitate the next step
        total = total + int(row[col:col + 1])

    if total > (len(diag) /2): # Use that total to see if we're adding one-columns to the output lists, or not
        for row in onesList:
            if row[col:col + 1] == "1": # Copy row to the target oxygenList if the current column has a 1
                oxygenList.append(row)


#
#
#
#
    
    onesList = oxygenList # Bump the target list we just sorted up to the source list, ready for the next iteration
    zerosList = scrubberList
    col += 1

# print(int(oxygenList[0],2))
# print(int(scrubberList[0],2))
print(len(oxygenList))
print(len(scrubberList))
