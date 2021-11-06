def main():

    data = read_input('2020/input/day5_input.txt')

    # Problem 1
    rows = []
    seats = []
    ids = []
    for entry in data:

        row = 63.5
        next_step = 128/2/2

        for i in range(7):
            if entry[i] == 'F':
                row -= next_step
            else:
                row += next_step
            next_step = next_step/2

        seat = 3.5
        next_step = 8/2/2
        for i in range(3):
            if entry[7+i] == 'L':
                seat -= next_step
            else:
                seat += next_step
            next_step = next_step/2

        rows.append(row)
        seats.append(seat)
        ids.append(int(row*8+seat))

    print(max(ids))

    # Problem 2:
    ids.sort()
    for i, entry in enumerate(ids):
        # If the next value is not 1 higher than we current value
        if (ids[i+1] - ids[i]) != 1:
            # Current value + 1 is not in the sorted list and therefore our seat id
            print(ids[i]+1)
            break


def read_input(filename):

    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
