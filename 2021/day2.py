def main():

    data = read_input('2021/input/day2.txt')

    horizontal = 0
    depth = 0

    # part 1
    for line in data:
        direction, value = line.split(' ')

        if direction == 'forward':
            horizontal += int(value)
        elif direction == 'down':
            depth += int(value)
        elif direction == 'up':
            depth -= int(value)

    print(horizontal*depth)

    # part 2
    horizontal = 0
    depth = 0
    aim = 0

    for line in data:
        direction, value = line.split(' ')

        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == 'down':
            aim += int(value)
        elif direction == 'up':
            aim -= int(value)

    print(horizontal*depth)


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
