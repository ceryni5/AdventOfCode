import itertools


def main():

    data = read_input('2020/input/day9_input.txt')
    data = [int(line) for line in data]

    # problem1
    for i in range(0, len(data)-25):
        preamble = data[i:i+25]
        check = data[i+25]

        combinations = list(itertools.combinations(preamble, 2))
        sums = [sum(values) for values in combinations]

        if check not in sums:
            p1 = check
            print(p1, 'is not okay')
            break

    for i in range(0, len(data)):
        for j in range(1, len(data)):
            sequence = data[i:j]
            if sum(sequence) == p1:
                print(sequence)
                print(min(sequence) + max(sequence))
                quit()
            if sum(sequence) > p1:
                break


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
