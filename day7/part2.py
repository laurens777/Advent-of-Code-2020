import re

def main():
    bags = {}
    with open("input.txt") as input:
        for line in input:
            line = line.strip("\n")
            try:
                outer = re.search('([a-z]+ [a-z]+) bags contain', line)
                inner = re.findall('([1-9] [a-z]+ [a-z]+) bag', line)
            except AttributeError:
                print("something went wrong")

            bags[outer.group(1)] = [bag for bag in inner]

    print(numBags(bags, "shiny gold"))

def numBags(bags, color):
    i = 0
    for bag in bags[color]:
        s = bag.split(" ", 1)
        if numBags(bags, s[1]) == 0:
            i += int(s[0])
        else:
            i += int(s[0]) + int(s[0])*numBags(bags, s[1])

    return i


if __name__ == "__main__":
    main()