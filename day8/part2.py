def checkCode(data):
    visited = []
    i = 0
    acc = 0
    term = True
    while i < len(data):
        if i in visited:
            term = False
            break
        visited.append(i)
        if data[i].split(' ')[0] == "nop":
            i += 1
        elif data[i].split(' ')[0] == "acc":
            acc += int(data[i].split(' ')[1])
            i += 1
        else:
            i += int(data[i].split(' ')[1])

    return term, acc

def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(line.strip('\n'))
        
    j = 0
    while j < len(data):
        if data[j].split(' ')[0] == "nop":
            dataCopy = data.copy()
            dataCopy[j] = "jmp " + data[j].split(' ')[1]
            term, acc = checkCode(dataCopy)
            if term == True:
                break
        elif data[j].split(' ')[0] == "jmp":
            dataCopy = data.copy()
            dataCopy[j] = "nop " + data[j].split(' ')[1]
            term, acc = checkCode(dataCopy)
            if term == True:
                break

        j += 1

    print("Acc value = ", acc)


if __name__ == "__main__":
    main()