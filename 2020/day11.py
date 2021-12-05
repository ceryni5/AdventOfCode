def main():

    data = read_input('2020/input/day11_input.txt')
    data = [list(line) for line in data]

    for row in data:
        for seat in row:

            if seat == 'L':

            count_neighbors()

        elif seat == '#':

            count_neighbors()

        elif seat '.':
            continue


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
