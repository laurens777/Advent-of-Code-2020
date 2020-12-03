def main():
    goodPass = 0
    with open("./input.txt") as f:
        for line in f:
            temp = line.split()
            i, j = temp[0].split('-')
            target = temp[1].strip(':')
            k=0
            if (temp[2][int(i)-1] == target) != (temp[2][int(j)-1] == target):
                goodPass += 1

    print("There are %i good passwords." % goodPass)

if __name__ == '__main__':
    main()