def main():

    data = read_input('2020/input/day10_input.txt')
    data = [int(line) for line in data]

    # data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    data.sort()

    if data[0] == 1:
        one_jolt = 1  # The first step i snot included in the loop
    else:
        one_jolt = 0

    if data[0] == 3:
        three_jolt = 2  # The first step i snot included in the loop
    else:
        three_jolt = 1  # since we have the last to the device

    for i in range(1, len(data)):
        if data[i] - data[i-1] == 1:
            one_jolt += 1
        if data[i] - data[i-1] == 3:
            three_jolt += 1

    print(one_jolt*three_jolt)

    # problem2
    data = [0] + data
    # data = data[0:4]
    print(data)

    ways_to_get_to = dict(zip(data, [1]*len(data)))

    # The number of ways to get to the last value is the sum of the
    # number of way to get to the values [-1], [-2] & [-3].
    # If they not exist (there is no entry), there are 0 ways.
    for pos in data[1:]:
        ways_to_get_to[pos] = ways_to_get_to.get(pos-1, 0) + \
            ways_to_get_to.get(pos-2, 0) + ways_to_get_to.get(pos-3, 0)

    print(ways_to_get_to)
    print(ways_to_get_to.get(data[-1]))


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
