def main():
    h = {}
    with open("./input.txt") as f:
        for line in f:
            x = int(line)
            if x not in h:
                y = 2020 - x
                h[y] = x
            else:
                print("%i + %i = 2020 \n%i * %i = %i" % (x, h[x], x, h[x], x*h[x]))
                return

if __name__ == '__main__':
    main()
