import math

def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(line.strip("\n"))

    facing = "E"
    ship = [0, 0]
    waypoint = [10, 1]
    for line in data:
        if line[0] == "N":
            waypoint[1] += int(line[1:])
            continue
        if line[0] == "S":
            waypoint[1] -= int(line[1:])
            continue
        if line[0] == "E":
            waypoint[0] += int(line[1:])
            continue
        if line[0] == "W":
            waypoint[0] -= int(line[1:])
            continue
        if line[0] == "F":
            x = int(line[1:]) * waypoint[0]
            y = int(line[1:]) * waypoint[1]
            ship[0] += x
            ship[1] += y
        if line[0] == "L":
            rotations = int(line[1:]) / 90
            for i in range(int(rotations)):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        if line[0] == "R":
            rotations = int(line[1:]) / 90
            for i in range(int(rotations)):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

    print(ship)


if __name__ == "__main__":
    main()