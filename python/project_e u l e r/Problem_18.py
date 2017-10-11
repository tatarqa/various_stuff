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
            data_list.append(row)


def analyze_input():
    data_list = []
    load_input(data_list)
    for ri, row in enumerate(data_list):
        for ni, nr in enumerate(row[:-1]):  # ignore last item in a row for it was calculated in previous round
            if ni == len(row) - 1:
                break
            if ni < len(row) - 1:
                index_add = 0
                if nr > row[ni + 1]:
                    top_in_pair = nr
                else:
                    top_in_pair = row[ni + 1]

            data_list[ri + 1][ni - index_add] += top_in_pair

    return data_list[len(data_list) - 1]


if __name__ == "__main__":
    print analyze_input()
