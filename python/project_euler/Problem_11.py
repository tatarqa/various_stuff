def verticalSum(obj, WIDTH, list1, list2, list3):
    for i, itom in enumerate(obj):
        diagonal_left_sum = 1
        diagonal_right_sum = 1
        vertical_sum = 1
        if i >= WIDTH - 1:
            sequence_list = [int(itom), int(list1[i - 1]), int(list2[i - 2]), int(list3[i - 3])]
            for nr in sequence_list:
                diagonal_left_sum *= nr
            yield diagonal_left_sum

        if i < len(obj) - (WIDTH - 1):
            sequence_list = [int(itom), int(list1[i + 1]), int(list2[i + 2]), int(list3[i + 3])]
            for nr in sequence_list:
                diagonal_right_sum *= nr
            yield diagonal_right_sum

        sequence_list = [int(itom), int(list1[i]), int(list2[i]), int(list3[i])]
        for nr in sequence_list:
            vertical_sum *= nr
        yield vertical_sum


def horizontalSum(obj, WIDTH):
    for i, itom in enumerate(obj):
        row_left_range_sum = 1
        row_right_range_sum = 1
        if i >= WIDTH - 1:
            sequence_list = []
            sequence_list.append(int(itom))
            for d in range(1, WIDTH):
                sequence_list.append(int(obj[i - d]))
            for nr in sequence_list:
                row_left_range_sum *= nr
            yield row_left_range_sum
        if i < len(obj) - (WIDTH - 1):
            sequence_list = []
            sequence_list.append(int(itom))
            for d in range(1, WIDTH):
                sequence_list.append(int(obj[i + d]))
            for nr in sequence_list:
                row_right_range_sum *= nr
            yield row_left_range_sum


def main():
    lists = []
    input = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n' \
            '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n' \
            '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n' \
            '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n' \
            '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n' \
            '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n' \
            '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n' \
            '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n' \
            '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n' \
            '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n' \
            '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n' \
            '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n' \
            '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n' \
            '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n' \
            '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n' \
            '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n' \
            '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n' \
            '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n' \
            '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n' \
            '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

    for line in input.splitlines():
        row = []
        for item in line.split():
            row.append(item)
        lists.append([row])

    WIDTH = 4
    iter_list = []
    for i, item in enumerate(lists):
        if i >= WIDTH - 1:
            prevlist_3 = lists[i - 3][0]
            prevlist_2 = lists[i - 2][0]
            prevlist_1 = lists[i - 1][0]
            iter_list.append(list(verticalSum(item[0], 4, prevlist_1, prevlist_2, prevlist_3)))
        iter_list.append(horizontalSum(item[0], 4))

    highestnr = 0
    for item in iter_list:
        for nr in item:
            if nr > highestnr:
                highestnr = nr

    print highestnr


if __name__ == "__main__":
    main()
