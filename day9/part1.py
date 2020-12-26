def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(int(line))

    for i in range(25, len(data)):
        target = data[i]
        h = {}
        found = True
        for j in range(i-25, i):
            if data[j] not in h:
                h[target - data[j]] = data[j]
            elif data[j] in h:
                break
            if j == i-1:
                found = False
        if found == False:
            print(target)
            break

if __name__ == "__main__":
    main()