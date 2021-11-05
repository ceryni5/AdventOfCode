import numpy as np
import math

# day 3


def main():

    # Get data
    data = np.array(read_input('2020/input/day3_input.txt'))

    # Problem 1
    y_pos = 0
    hit_trees = 0
    width = len(data[0])

    for x, line in enumerate(data):
        if data[x][y_pos] == '#':
            hit_trees += 1

        y_pos = (y_pos+3) % width

    print(hit_trees)

    # Problem 2
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    print(math.prod([trees_on_slope(entry[0], entry[1], data) for entry in slopes]))


def read_input(filename):

    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


def trees_on_slope(right, down, data):

    y_pos = 0
    x_pos = 0
    hit_trees = 0
    width = len(data[0])

    while(x_pos < len(data)):
        if data[x_pos][y_pos] == '#':
            hit_trees += 1

        y_pos = (y_pos+right) % width
        x_pos = (x_pos+down)

    return hit_trees


if __name__ == '__main__':
    main()
