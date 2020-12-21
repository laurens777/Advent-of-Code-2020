def main():
    result = 0
    with open("./input.txt") as input:
        questions = {}
        i = 0
        for line in input:
            if line == "\n":
                for item in questions:
                    if questions[item] == i:
                        result += 1
                questions.clear()
                i = 0
                continue
            i += 1
            line = line.strip('\n')
            for ch in line:
                if ch in questions:
                    questions[ch] += 1
                else:
                    questions[ch] = 1
    for item in questions:
        if questions[item] == i:
            result += 1

    print(result)
    return


if __name__ == "__main__":
    main()