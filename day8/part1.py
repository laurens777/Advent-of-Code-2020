def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(line.strip('\n'))
        
    visited = []
    i = 0
    acc = 0
    while i <= len(data):
        if i in visited:
            break
        visited.append(i)
        if data[i].split(' ')[0] == "nop":
            i += 1
        elif data[i].split(' ')[0] == "acc":
            acc += int(data[i].split(' ')[1])
            i += 1
        else:
            i += int(data[i].split(' ')[1])

    print("Acc value = ", acc)


if __name__ == "__main__":
    main()