def load_input(data_list):
    with open("Problem_18_input.txt", 'r') as input_file:
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


def analyze_input(start_routes):
    data_list = []
    load_input(data_list)
    final_routes = ()
    final_sum = 0
    for c, data_row in enumerate(data_list):
        found = False
        d = 0
        for line in get_n_highest_numbers(data_row):
            highest_numbers = line
        while found != True:
            if d < len(data_row):
                number = data_row[d]
            else:
                print 'FAIL'
                return False
            if number in highest_numbers:
                if final_routes is not ():
                    if final_routes[1] in range(d - 1, d + 1):
                        final_routes = (number, d)
                        found = True

                else:
                    if (number, d) not in start_routes:
                        final_routes = (number, d)
                        start_routes.append(final_routes)
                        found = True

            if found is True:
                final_sum += number
                if c == (len(data_list) - 1):
                    print final_sum
                    return True
            d += 1


def main():
    not_finished = True
    first_routes = []
    result = analyze_input(first_routes)
    while not_finished is True:
        if not result:
            result = analyze_input(first_routes)
        else:
            not_finished = False


if __name__ == "__main__":
    main()
