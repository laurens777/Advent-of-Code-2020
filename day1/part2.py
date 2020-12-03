import time

# A simple n^3 algorithm 
# Can be improved slightly using while loops and ensuring j > i and k > j
def bruteForce(input):
    for i in input:
        for j in input:
            for k in input:
                if i+j+k == 2020:
                    return (i, j, k)

# this is the standard 3SUM algorithm
# psuedo-code can be found on wikipedia
def threeSum(input):
    input.sort()
    for i in range(0,len(input)-2):
        start = i+1
        end = len(input)-1
        while start < end:
            if input[start]+input[end]+input[i] == 2020:
                return (input[start],input[end],input[i])
            elif input[start]+input[end]+input[i] > 2020:
                end -= 1
            else:
                start += 1

# this was an idea given to me by someone else
# this uses my solution from part1 and generalizes it to 3SUM
# this solution is still slightly slower than the algo above
def threeSum2(input):
    for i in range(0,len(input)):
        d = {}
        target = 2020-input[i]
        for j in range(i+1, len(input)):
            x = input[j]
            if x not in d:
                y = target - x
                d[y] = x
            else:
                return (input[i], x, d[x])

def time_calc(label, do_calc, arr):
    st = time.time()
    for _ in range(10):
        do_calc(arr)
    en = time.time()
    print("%s: %g seconds" % (label, (en-st)/10))

def main():
    listNums = []
    with open("input.txt") as f:
        for i in f:
            listNums.append(int(i))
    
    time_calc("Brute force", bruteForce, listNums)
    time_calc("part1 algo", threeSum2, listNums)
    time_calc("fast algo", threeSum, listNums)


if __name__ == '__main__':
    main()