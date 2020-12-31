from copy import deepcopy

def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(list(line.strip('\n')))

    iteration = 0
    changed = True
    while changed == True:
        changed = False
        newData = deepcopy(data)
        for x in range(0, len(data)):
            for y in range(0, len(data[x])):
                if data[x][y] == ".":
                    continue
                elif data[x][y] == "L":
                    count = checkPosition(data, x, y)
                    if count == 0:
                        newData[x][y] = "#"
                        changed = True
                else:
                    count = checkPosition(data, x, y)
                    if count >= 4:
                        newData[x][y] = "L"
                        changed = True
        print("Iteration", iteration, "completed")
        iteration += 1
        data = newData

    occSeats = 0
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            if data[x][y] == "#":
                occSeats += 1

    print("There are", occSeats, "occupied.")

def checkPosition(data, x, y):
    count = 0
    for i in range(x-1,x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            if i >= len(data) or j >= len(data[i]):
                continue
            if i == x and j == y:
                continue
            if data[i][j] == "#":
                    count += 1
    return count

if __name__ == "__main__":
    main()