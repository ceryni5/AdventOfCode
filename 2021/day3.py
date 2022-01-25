import numpy as np


def main():

    data = read_input('2021/input/day3.txt')

    # part 1
    c = ''
    e = ''
    for pos in range(len(data[0])):

        ones = 0
        zeros = 0
        for line in data:
            if line[pos] == '1':
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            c += '1'
            e += '0'
        else:
            c += '0'
            e += '1'

    print(int(c, 2)*int(e, 2))

    # part 2

    # keep most common
    data_1 = np.asarray([list(line) for line in data])
    for pos in range(len(data_1[0])):

        if len(data_1) == 1:
            break

        mean = np.mean(data_1[:, pos].astype(int))
        filter_crit = 1 if mean >= 0.5 else 0

        filter = np.where(data_1[:, pos] == str(filter_crit))

        data_1 = data_1[filter]

    # keep least common
    data_2 = np.asarray([list(line) for line in data])
    for pos in range(len(data_2[0])):

        if len(data_2) == 1:
            break

        mean = np.mean(data_2[:, pos].astype(int))
        filter_crit = 1 if mean >= 0.5 else 0

        filter = np.where(data_2[:, pos] != str(filter_crit))

        data_2 = data_2[filter]

    print(int(''.join(data_1[0]), 2) * int(''.join(data_2[0]), 2))


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
