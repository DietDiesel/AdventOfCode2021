commands = []

with open("02A\day2input.txt") as f:
    commands = f.readlines()

print(commands[0][:-3])
print(commands[0][-2:-1])