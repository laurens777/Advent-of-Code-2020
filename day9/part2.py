def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(int(line))

    for i in range(0,len(data)):
        j = i
        total = 0
        smallest = data[i]
        largest = data[i]
        while total < 1398413738:
            total += data[j]
            if data[j] < smallest:
                smallest = data[j]
            if data[j] > largest:
                largest = data[j]
            j += 1
        if total == 1398413738:
            print(smallest + largest)
            break

if __name__ == "__main__":
    main()