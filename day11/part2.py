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
                    if count >= 5:
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
    l = [x, y-1]
    r = [x, y+1]
    u = [x-1, y]
    d = [x+1, y]
    lu = [x-1, y-1]
    ld = [x+1, y-1]
    ru = [x-1, y+1]
    rd = [x+1, y+1]
    while True:
        if l[1] < 0 or data[l[0]][l[1]] == "L":
            break
        if data[l[0]][l[1]] == "#":
            count += 1
            break
        l[1] -= 1
    while True:
        if r[1] >= len(data[x]) or data[r[0]][r[1]] == "L":
            break
        if data[r[0]][r[1]] == "#":
            count += 1
            break
        r[1] += 1
    while True:
        if u[0] < 0 or data[u[0]][u[1]] == "L":
            break
        if data[u[0]][u[1]] == "#":
            count += 1
            break
        u[0] -= 1
    while True:
        if d[0] >= len(data) or data[d[0]][d[1]] == "L":
            break
        if data[d[0]][d[1]] == "#":
            count += 1
            break
        d[0] += 1
    while True:
        if lu[0] < 0 or lu[1] < 0 or data[lu[0]][lu[1]] == "L":
            break
        if data[lu[0]][lu[1]] == "#":
            count += 1
            break
        lu[0] -= 1
        lu[1] -= 1
    while True:
        if ru[1] >= len(data[x]) or ru[0] < 0 or data[ru[0]][ru[1]] == "L":
            break
        if data[ru[0]][ru[1]] == "#":
            count += 1
            break
        ru[1] += 1
        ru[0] -= 1
    while True:
        if ld[1] < 0 or ld[0] >= len(data) or data[ld[0]][ld[1]] == "L":
            break
        if data[ld[0]][ld[1]] == "#":
            count += 1
            break
        ld[1] -= 1
        ld[0] += 1
    while True:
        if rd[0] >= len(data) or rd[1] >= len(data[x]) or data[rd[0]][rd[1]] == "L":
            break
        if data[rd[0]][rd[1]] == "#":
            count += 1
            break
        rd[0] += 1
        rd[1] += 1


    return count

if __name__ == "__main__":
    main()