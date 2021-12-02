commands = []

with open("02A\day2input.txt") as f:
    commands = f.readlines()

depth = 0
hPosition = 0



for cmd in commands:
    print("command", cmd[:2])
    if cmd[:2] == "fo":
        print("forward", cmd[8:9])
        hPosition = hPosition + int(cmd[8:9])
    elif cmd[:2]== "up":
        print("up", cmd[3:4])
        depth = depth - int(cmd[3:4])
    elif cmd[:2]== "do":
        print("down", cmd[5:6])
        depth = depth + int(cmd[5:6])
    
print("hPosition", hPosition)
print("depth", depth)
print("answer", hPosition * depth)