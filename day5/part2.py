import math

def main():
    fullSeats = []
    with open("./input.txt") as input:
        for seat in input:
            i = 0
            row = (0, 127)
            while i < 6:
                if seat[i] == 'F':
                    middle = row[0] + math.floor((row[1]-row[0])/2)
                    row = (row[0], middle)
                else:
                    middle = row[0] + math.ceil((row[1]-row[0])/2)
                    row = (middle, row[1])
                i+=1
            seatRow = row[0] if seat[6] == 'F' else row[1]

            column = (0,7)
            j = 7
            while j < 9:
                if seat[j] == 'L':
                    middle = column[0] + math.floor((column[1]-column[0])/2)
                    column = (column[0], middle)
                else:
                    middle = column[0] + math.ceil((column[1]-column[0])/2)
                    column = (middle, column[1])
                j+=1
            seatColumn = column[0] if seat[9] == 'L' else column[1]

            fullSeats.append(seatRow*8+seatColumn)

    fullSeats.sort()
    for i in range(len(fullSeats)):
        if i not in fullSeats:
            print(i)

if __name__ == "__main__":
    main()