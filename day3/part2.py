def main():
    tree1, tree2, tree3, tree4, tree5 = 0, 0, 0, 0, 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    i = 0
    with open("input.txt") as input:
        for line in input:
            if line[s1 % len(line.strip('\n'))] == "#":
                tree1 += 1
            if line[s2 % len(line.strip('\n'))] == "#":
                tree2 += 1
            if line[s3 % len(line.strip('\n'))] == "#":
                tree3 += 1
            if line[s4 % len(line.strip('\n'))] == "#":
                tree4 += 1
            if i % 2 == 0:
                if line[s5 % len(line.strip('\n'))] == "#":
                    tree5 += 1
                s5 += 1
 
            s1 += 1
            s2 += 3
            s3 += 5
            s4 += 7
            i += 1
        print(tree1 * tree2 * tree3 * tree4 * tree5)

if __name__ == '__main__':
    main()