nrs_dict = {
    1: ('one', ''),
    2: ('two', 'twen'),
    3: ('three', 'thir'),
    4: ('four', 'for'),
    5: ('five', 'fif'),
    6: ('six', 'six'),
    7: ('seven', 'seven'),
    8: ('eight', 'eigh'),
    9: ('nine', 'nine'),
    10: ('ten', ''),
    11: ('Eleven', ''),
    12: ('Twelve', ''),
    13: ('Thirteen', ''),
    14: ('Fourteen', ''),
    15: ('Fifteen', ''),
    16: ('Sixteen', ''),
    17: ('Seventeen', ''),
    18: ('Eighteen', ''),
    19: ('Nineteen', ''),
    'tens': ('ty', ''),
    'hundreds': ('hundred', ''),
    'and': 'and'
}


def nr_to_word(number):
    word = ''
    while number > 0:
        if number <= 19:
            word += nrs_dict[number][0]
            break
        numLen = len(str(number))
        firstNumber = number / 10 ** (numLen - 1) % 10
        baseNum = (10 ** (numLen - 1)) * firstNumber
        rest_of_nr = number % baseNum
        if numLen == 2:
            word += nrs_dict[firstNumber][1]
            word += nrs_dict['tens'][0]
        elif numLen == 3:
            word += nrs_dict[firstNumber][0]
            word += nrs_dict['hundreds'][0]
            if not number % 100 == 0:
                word += nrs_dict['and']
        elif numLen == 4:
            yield 'onethousand'
        number = rest_of_nr
    yield word


NRS_RANGE = 1000
final_sequence = ''
for i in range(1, NRS_RANGE + 1):
    for word in nr_to_word(i):
        final_sequence += word
        print word
print final_sequence
print len(final_sequence)
