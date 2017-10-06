alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
            14: 'n',
            15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


def load_input():
    name = ''
    nr = 0
    with open("Problem_22_input.txt", 'r') as input_file:
        for line in input_file.readlines():
            for char in line.strip('"'):
                if char == ',' :
                    yield (name, nr)
                    name = ''
                    nr = 0
                else:
                    for i, char_in_dict in alphabet.iteritems():
                        if char_in_dict.upper() == char:
                            nr += i
                            name += char
                            break


def sumarize():
    sum = 0
    final_list = sorted(list(load_input()), key=lambda tup: tup[0])
    for i, line in enumerate((final_list), start=1):
        sum += i * line[1]
    return sum


if __name__ == "__main__":
    print sumarize()
