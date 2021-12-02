
lines = []

with open("01A\puzzInput.txt") as f:
    lines = f.readlines()

for i in lines:
    i = int(i)  

count = 0
i = 0

while i < len(lines) - 1:
    if lines[i] < lines[i + 1]:
        count = count + 1
    i = i + 1

# if lines[i] < lines[len(lines)]:
#     count = count + 1

print("final count is", count)
