def main():

    data = read_input('2020/input/day8_input.txt')

    # Problem1
    acc = 0
    active_i = 0
    visited_i = []
    print(data)
    while True:

        if active_i in visited_i:
            print(acc)
            break

        visited_i.append(active_i)
        line = data[active_i]

        if line[0:3] == 'acc':
            acc += int(line.split(' ')[1])
            active_i += 1
        if line[0:3] == 'nop':
            active_i += 1
        if line[0:3] == 'jmp':
            active_i += int(line.split(' ')[1])

    # Problem 2
    fixed = False
    for i, line in enumerate(data):

        # Check for 'nop', replace with 'jmp', run the program and revert the change
        if line[0:3] == 'nop':
            data[i] = 'jmp ' + line.split(' ')[1]
            fixed = run_the_program(data, 0, 0, [])
            data[i] = 'nop ' + line.split(' ')[1]

        # Same but replace jmps with nops
        if line[0:3] == 'jmp':
            data[i] = 'nop ' + line.split(' ')[1]
            fixed = run_the_program(data, 0, 0, [])
            data[i] = 'jmp ' + line.split(' ')[1]

        if fixed:
            break


def run_the_program(data, acc, active_i, visited_i):

    while True:

        # Break and continue if the change didn't fix the program
        if active_i in visited_i:
            return False

        # Break and return true is we try to access a line outside the program
        if active_i >= len(data):
            print('The program is fixed! The final acc value ist: ', acc)
            return True

        visited_i.append(active_i)
        line = data[active_i]

        # If acc, do the acc
        if line[0:3] == 'acc':
            acc += int(line.split(' ')[1])
            active_i += 1

        # If nop, try jumping
        if line[0:3] == 'nop':
            active_i += 1

        # And in case of jump, try to top
        if line[0:3] == 'jmp':
            active_i += int(line.split(' ')[1])

    return


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


if __name__ == '__main__':
    main()
