def load_input(data_list):
    with open("Problem_67_input.txt", 'r') as input_file:
        for line in reversed(input_file.readlines()):
            text_block = ''
            row = []
            for c in line.strip():
                if c.isdigit():
                    text_block += c
                else:
                    row.append(int(text_block))
                    text_block = ''
            row.append(int(text_block))  # last item in row..
            data_list.append(tuple(row))


def get_n_highest_numbers(numbers):
    row_len = len(numbers)
    if row_len > 4:
        highest_numbers = sorted(numbers, key=int, reverse=True)[:row_len / 4 + 2]
    else:
        highest_numbers = numbers
    yield highest_numbers


def analyze_input():
    data_list = []
    load_input(data_list)
    final_route = ()
    for data_row in data_list:
        found = False
        d = 0
        for line in get_n_highest_numbers(data_row):
            highest_numbers = line
        while found != True:
            number = data_row[d]
            if number in highest_numbers:
                if final_route is not ():
                    if final_route[1] < d:
                        return False
                        # TODO repeat the script using different values
                    if final_route[1] in range(d - 1, d):
                        final_route = (number, d)
                        found = True
                else:
                    final_route = (number, d)
                    found = True
            d += 1


def main():
    if analyze_input() == False:
        print 'It does not work'


if __name__ == "__main__":
    main()
