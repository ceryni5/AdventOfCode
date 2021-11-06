import re

# day 4


def main():

    # read in data, read in already splits at '\n\n'
    data = read_input('2020/input/day4_input.txt')
    # Remove the linebreak at the very end
    data[-1] = data[-1].strip()

    # Split the entries at ' |\n' into the field-values paires
    data = [re.split(' |\n', entry) for entry in data]

    # Split the field into key, value pairs
    data = [[field.split(':') for field in entry] for entry in data]

    # Problem 1
    # Check if the keys exists
    list_of_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' is missing
    problem1 = []
    for entry in data:
        fields = {}
        for elem in entry:
            fields[elem[0]] = elem[1]

        problem1.append(all(x in fields.keys() for x in list_of_keys))

    print(sum(problem1))

    # Problem 2
    list_of_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' is missing
    problem2 = []
    for entry in data:
        fields = {}
        for elem in entry:
            fields[elem[0]] = elem[1]

        # Case that all the keys exist:
        if all(x in fields.keys() for x in list_of_keys):

            birth_year = 1920 <= int(fields['byr']) <= 2002
            issue_year = 2010 <= int(fields['iyr']) <= 2020
            experition_year = 2020 <= int(fields['eyr']) <= 2030
            height = bool(
                re.search('^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$', fields['hgt']))
            hair_color = bool(re.search('^#[a-f0-9]{6}$', fields['hcl']))
            eye_color = fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            passport_id = bool(re.search('^[0-9]{9}$', fields['pid']))

            problem2.append(birth_year & issue_year & experition_year &
                            height & hair_color & eye_color & passport_id)

        else:
            problem2.append(False)

    print(sum(problem2))


def read_input(filename):

    data = ''
    with open(filename) as file:
        for line in file:
            data += line

    return data.split('\n\n')


if __name__ == '__main__':
    main()
