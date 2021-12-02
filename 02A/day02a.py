commands = []

with open("02A\day2input.txt") as f:
    commands = f.readlines()

print(int(commands[0][-2:-1]) + int(commands[1][-2:-1]))

for cmd in commands:
    print(cmd[:-3])
    print(int(cmd[-2:-1]))