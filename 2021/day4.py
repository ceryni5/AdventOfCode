import numpy as np


def read_input(filename):
    with open(filename) as file:
        data = [line.rstrip() for line in file]

    return data


def main():
    filename = '2021/input/day4.txt'

    # Read in all the stuff
    boards = []
    with open(filename) as file:
        numbers = list(map(int, file.readline().split(',')))
        board = []

        while (row := file.readline()) != '':

            if row == '\n':
                boards.append(np.asarray(board))
                board = []
            else:
                board.append(list(map(int, row.rstrip().split())))

    boards = boards[1:]

    # Part 1
    checks = [np.full((5, 5), False) for board in boards]
    found = False
    for number in numbers:

        if found:
            break

        for board, check in zip(boards, checks):

            # Update the check board
            check[np.where(board == number)] = True

            # Check for complete rows or columns on the check board
            # axis 0 is Trues along rows, axis 1 is Trues along columns
            axis0 = np.all(check, axis=0)
            axis1 = np.all(check, axis=1)

            if np.any(axis0) or np.any(axis1):
                print(number * sum(board[~check]))
                found = True
                break

    # Part 2
    checks = [np.full((5, 5), False) for board in boards]
    for number in numbers:

        for idx, (board, check) in enumerate(zip(boards, checks)):

            # Update the check board
            check[np.where(board == number)] = True

            # Check for complete rows or columns on the check board
            # axis 0 is Trues along rows, axis 1 is Trues along columns
            axis0 = np.all(check, axis=0)
            axis1 = np.all(check, axis=1)

            if np.any(axis0) or np.any(axis1):

                lastest_board_idx = idx


    last_board = boards[lastest_board_idx]
    check = np.full((5, 5), False)

    for number in numbers:
        check[np.where(last_board == number)] = True

        axis0 = np.all(check, axis=0)
        axis1 = np.all(check, axis=1)

        if np.any(axis0) or np.any(axis1):

            print(number)
            break


if __name__ == '__main__':
    main()
