
lines = []

with open("01A\puzzInput.txt") as f:
    lines = f.readlines()

for i in lines:
    i = int(i)  

count = 0
i = 0

# print(type(lines[i]))
while i < len(lines) - 3:
    print("Measurement", i)
    a = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
    print("\tWindow A is", a)
    b = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])
    print("\tWindow B is", b)
    if a < b:
        print("\tA is less than B, so increasing count")
        count = count + 1
    i = i + 1

print("final count is", count)