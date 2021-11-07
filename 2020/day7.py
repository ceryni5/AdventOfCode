import re
import math


def main():
    data = read_input('2020/input/day7_input.txt')
    # data = data[0:111]
    data = [re.split('contain|,', entry) for entry in data]

    bags = []
    must_contain = []
    contain_number = []
    for entry in data:

        bags.append(entry[0][0:-6])

        must_contain.append([entry[i].split('bag')[0][3:-1]
                            for i in range(1, len(entry))])
        contain_number.append([int(entry[i].split('bag')[0][1].replace('n', '0'))
                               for i in range(1, len(entry))])

    '''
    for bag, must, number in zip(bags, must_contain, contain_number):
        print(bag, must, number)
    '''

    is_contained = []
    for entry1 in bags:

        temp_list = []
        for i, entry2 in enumerate(must_contain):

            if entry1 in entry2:
                # print(f'{entry1} is in {bags[i]}')
                temp_list.append(bags[i])

        is_contained.append(temp_list)

    '''
    for bag, must_contain, is_contained in zip(bags, must_contain, is_contained):
        print(bag, must_contain, is_contained)
    '''
    problem1 = is_contained_in('shiny gold', bags, must_contain, is_contained, [])

    global problem2
    problem2 = 0
    contains_bags('shiny gold', bags, must_contain, contain_number, 1)

    print(len(set(problem1)))
    print(problem2)


def is_contained_in(search, bags, must_contain, is_contained, result):

    for bag, contain, contained in zip(bags, must_contain, is_contained):

        if bag == search:

            for value in contained:
                result.append(value)
                is_contained_in(value, bags, must_contain, is_contained, result)

    return result


def contains_bags(search, bags, must_contain, contain_number, number_of_bags):

    global problem2
    for bag, contain, number in zip(bags, must_contain, contain_number):

        if bag == search:

            for color, n in zip(contain, number):

                problem2 += n*number_of_bags
                if n != 0:
                    contains_bags(color, bags, must_contain, contain_number, number_of_bags*n)

    return


def read_input(filename):

    with open(filename) as file:
        data = [line.rstrip().replace('.', '') for line in file]

    return data


if __name__ == '__main__':
    main()
