import numpy as np


def main():

    data = read_input('2020/input/day2_input.txt')

    data = np.array([line.rstrip().split(' ') for line in data])

    # Problem 1 in one line
    print(sum([
        list(map(int, line[0].split('-')))[0] <=
        line[2].count(line[1][0]) <=
        list(map(int, line[0].split('-')))[1]
        for line in data]))

    # Problem 2
    print(sum([
        (line[2][list(map(int, line[0].split('-')))[0]-1] == line[1][0])
        ^
        (line[2][list(map(int, line[0].split('-')))[1]-1] == line[1][0])
        for line in data
    ]))


def read_input(filename):

    with open(filename) as file:
        data = [line for line in file]

    return data


if __name__ == '__main__':
    main()
