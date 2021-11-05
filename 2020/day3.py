import numpy as np

# day 3


def main():

    data = np.array(read_input('2020/input/day3_input.txt'))

    y_pos = 0
    hit_trees = 0
    width = len(data[0])

    for x, line in enumerate(data):
        if data[x][y_pos] == '#':
            hit_trees += 1

        y_pos = (y_pos+3) % width

    print(hit_trees)


def read_input(filename):

    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
