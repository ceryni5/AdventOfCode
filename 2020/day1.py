# Day 1, puzzle 1
import itertools


def main():

    values = read_values()

    two_that_equal_2020(values)

    three_that_equal_2020(values)


def read_values():

    filename = '2020/input/day1_input.txt'

    values = []

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            values.append(int(line))

    return values


def two_that_equal_2020(values):

    for entry in values:
        if (2020 - entry) in values:
            print(f'The which equal 2020 when added are: {entry} & {2020 - entry}.')
            print(f'Thier product is {entry * (2020-entry)}.')
            break


def three_that_equal_2020(values):

    for first_number, second_number in itertools.product(values, values):
        if (third_number := 2020 - first_number - second_number) in values:
            print(f'The three numbers are {first_number}, {second_number} & {third_number}.')
            print(f'Thier product is {first_number*second_number*third_number}')
            break


if __name__ == '__main__':
    main()
