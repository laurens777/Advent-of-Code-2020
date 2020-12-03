def main():
    tree1 = 0
    s1 = 0
    with open("input.txt") as input:
        for line in input:
            if line[s1 % len(line.strip('\n'))] == "#":
                tree1 += 1
            s1 += 3
        print(tree1)

if __name__ == '__main__':
    main()