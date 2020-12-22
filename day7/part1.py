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

            bags[outer.group(1)] = [re.sub('[1-9] ', '', bag) for bag in inner]

    result = set()

    for bag, content in bags.items():
        if "shiny gold" in content:
            result.add(bag)

    for i in range(len(bags)):
        for bag, content in bags.items():
            for res in result.copy():
                if res in content:
                    result.add(bag)

    print(len(result))


if __name__ == "__main__":
    main()