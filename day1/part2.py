def main():
    listNums = []
    with open("input.txt") as f:
        for i in f:
            listNums.append(int(i))
    
    for i in listNums:
        for j in listNums:
            for k in listNums:
                if i+j+k == 2020:
                    print(i*j*k)
                    return

if __name__ == '__main__':
    main()