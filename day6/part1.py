def main():
    result = 0
    with open("./input.txt") as input:
        questions = set()
        for line in input:
            if line == "\n":
                result += len(questions)
                questions.clear()
                continue
            line = line.strip('\n')
            for ch in line:
                questions.add(ch)
    result += len(questions)


    print(result)
    return


if __name__ == "__main__":
    main()