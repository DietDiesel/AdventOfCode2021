commands = []

with open("02A\day2input.txt") as f:
    commands = f.readlines()

depth = 0
hPosition = 0
aim = 0

for cmd in commands:

    if cmd[:2] == "fo":
        speed = int(cmd[8:9])
        hPosition = hPosition + speed
        depth = depth + (speed * aim)

    elif cmd[:2] == "up":
        aim = aim - int(cmd[3:4])

    elif cmd[:2] == "do":
        aim = aim + int(cmd[5:6])

print("hPosition", hPosition)
print("depth", depth)
print("answer", hPosition * depth)