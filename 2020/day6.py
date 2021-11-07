
def main():

    data = read_input('2020/input/day6_input.txt')
    data[-1] = data[-1].strip()

    # Problem 1
    # Get rid of all the linebreaks
    data1 = [entry.replace('\n', '') for entry in data]

    problem1 = [len(set(entry)) for entry in data1]
    print(sum(problem1))

    # problem2
    data2 = [entry.split('\n') for entry in data]

    problem2 = []
    for group in data2:
        intersect = group[0]
        for person in group:
            intersect = set(intersect).intersection(person)

        problem2.append(len(intersect))

    print(sum(problem2))


def read_input(filename):

    data = ''
    with open(filename) as file:
        for line in file:
            data += line

    return data.split('\n\n')


if __name__ == '__main__':
    main()
