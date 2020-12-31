import math

def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(line.strip("\n"))

    facing = "E"
    xPos = 0
    yPos = 0
    for line in data:
        if line[0] == "N":
            yPos += int(line[1:])
            continue
        if line[0] == "S":
            yPos -= int(line[1:])
            continue
        if line[0] == "E":
            xPos += int(line[1:])
            continue
        if line[0] == "W":
            xPos -= int(line[1:])
            continue
        if line[0] == "F":
            if facing == "N":
                yPos += int(line[1:])
                continue
            if facing == "S":
                yPos -= int(line[1:])
                continue
            if facing == "E":
                xPos += int(line[1:])
                continue
            if facing == "W":
                xPos -= int(line[1:])
                continue
        if line[0] == "L" and line[1:] == "180" or line[0] == "R" and line[1:] == "180":
            if facing == "N":
                facing = "S"
                continue
            if facing == "S":
                facing = "N"
                continue
            if facing == "E":
                facing = "W"
                continue
            if facing == "W":
                facing = "E"
                continue
        if line[0] == "L" and line[1:] == "270" or line[0] == "R" and line[1:] == "90":
            if facing == "N":
                facing = "E"
                continue
            if facing == "S":
                facing = "W"
                continue
            if facing == "E":
                facing = "S"
                continue
            if facing == "W":
                facing = "N"
                continue
        if line[0] == "L" and line[1:] == "90" or line[0] == "R" and line[1:] == "270":
            if facing == "N":
                facing = "W"
                continue
            if facing == "S":
                facing = "E"
                continue
            if facing == "E":
                facing = "N"
                continue
            if facing == "W":
                facing = "S"
                continue

    print(abs(xPos) + abs(yPos))


if __name__ == "__main__":
    main()