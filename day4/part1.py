def main():
    data = []
    passport = {}
    with open("./input.txt") as input:
        for line in input:
            if line == "\n":
                data.append(passport)
                passport = {}
                continue

            l = line.strip("\n").split(" ")
            for i in l:
                passport[i.split(":")[0]] = i.split(":")[1]
    l = line.strip("\n").split(" ")
    for i in l:
        passport[i.split(":")[0]] = i.split(":")[1]
    data.append(passport)

    need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    for i in data:
        result = all(keys in i for keys in need)
        if result:
            count += 1

    print(count)

if __name__ == "__main__":
    main()