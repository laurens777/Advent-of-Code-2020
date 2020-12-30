def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(int(line))

    quickSort(data, 0, len(data)-1)

    one = 0
    three = 0
    i = 0
    if data[0] == 1:
        one += 1
    elif data[0] == 3:
        three += 1
    while i < len(data)-1:
        if data[i+1] - data[i] == 1:
            one += 1
        elif data[i+1] - data[i] == 3:
            three += 1
        
        i += 1

    print(one, three)
    print(one * (three+1))


def quickSort(ls, p, r):
    if p < r:
        q = partition(ls, p, r)
        quickSort(ls, p , q-1)
        quickSort(ls, q+1, r)

def partition(ls, p, r):
    x = ls[r]
    i = p-1
    for j in range(p, r):
        if ls[j] <= x:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]

    ls[i+1], ls[r] = ls[r], ls[i+1]
    return i+1

if __name__ == "__main__":
    main()