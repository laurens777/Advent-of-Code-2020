import re

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
        if not all(keys in i for keys in need):
            continue
        if not ((int(i["byr"]) >= 1920) and (int(i["byr"]) <= 2002)):
            continue
        if not ((int(i["iyr"]) >= 2010) and (int(i["iyr"]) <= 2020)):
            continue
        if not ((int(i["eyr"]) >= 2020) and (int(i["eyr"]) <= 2030)):
            continue
        if not re.match("([0-9]{1,4}(in|cm))", i["hgt"]):
            continue
        if re.match("[0-9]{1,4}in", i["hgt"]):
            if not ((int(i["hgt"].strip("in")) >= 59) and (int(i["hgt"].strip("in")) <= 76)):
                continue
        if re.match("[0-9]{1,4}cm", i["hgt"]):
            if not ((int(i["hgt"].strip("cm")) >= 150) and (int(i["hgt"].strip("cm")) <= 193)):
                continue
        if not i["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]:
            continue
        if not re.match("#([a-f]|[0-9]){6}", i["hcl"]):
            continue
        if not re.match("\A[0-9]{9}\Z", i["pid"]):
            continue
        count += 1

    print("result: ", count)

if __name__ == "__main__":
    main()