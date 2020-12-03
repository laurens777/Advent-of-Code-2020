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
            fullLine = line.strip("\n")*1000000
            if fullLine[s1] == "#":
                tree1 += 1
            if fullLine[s2] == "#":
                tree2 += 1
            if fullLine[s3] == "#":
                tree3 += 1
            if fullLine[s4] == "#":
                tree4 += 1
            if i % 2 == 0:
                if fullLine[s5] == "#":
                    tree5 += 1
                s5 += 1
 
            s1 += 1
            s2 += 3
            s3 += 5
            s4 += 7
            i += 1
        print(tree1, tree2, tree3, tree4, tree5)

if __name__ == '__main__':
    main()