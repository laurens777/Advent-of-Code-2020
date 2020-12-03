def main():
    goodPass = 0
    with open("./input.txt") as f:
        for line in f:
            temp = line.split()
            i, j = temp[0].split('-')
            target = temp[1].strip(':')
            k=0
            for letter in temp[2]:
                if letter == target:
                    k += 1
            if k >= int(i) and k <= int(j):
                goodPass += 1

    print("There are %i good passwords." % goodPass)

if __name__ == '__main__':
    main()