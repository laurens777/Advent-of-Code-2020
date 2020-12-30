def main():
    data = []
    with open("input.txt") as input:
        for line in input:
            data.append(int(line))

    quickSort(data, 0, len(data)-1)

    data.append(data[-1]+3)

    counts = {0:1}

    for jolt in data:
        j1,j2,j3 = 0,0,0
        if jolt-1 in counts:
            j1 = counts[jolt-1]
        if jolt-2 in counts:
            j2 = counts[jolt-2]
        if jolt-3 in counts:
            j3 = counts[jolt-3]
        counts[jolt] = j1 + j2 + j3

    print(counts)

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