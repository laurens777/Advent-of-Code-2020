def main():
    tree1 = 0
    s1 = 0
    with open("input.txt") as input:
        for line in input:
            fullLine = line.strip("\n")*1000
            if fullLine[s1] == "#":
                tree1 += 1
            s1 += 3
        print(tree1)

if __name__ == '__main__':
    main()