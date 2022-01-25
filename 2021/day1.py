def main():

    data = read_input('2021/input/day1.txt')

    deeper = []
    depth = data[0]
    for line in data:
        deeper.append(line > depth)
        depth = line

    print(sum(deeper))

    deeper = []
    depth = sum(data[0:3])
    for idx, l in enumerate(data):
        deeper.append(sum(data[idx:idx+3]) > depth)
        depth = sum(data[idx:idx+3])

    print(sum(deeper))


def read_input(filename):
    with open(filename) as file:
        data = [int(line.rstrip()) for line in file]

    return data


if __name__ == '__main__':
    main()
