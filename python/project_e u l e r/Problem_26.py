import sys

sys.setrecursionlimit(1200)


class Problem_26(object):
    def solution(self, dividend, divisor, longest_seq):
        vysledek = ''
        remainders = []
        seq = []
        i = 0
        seq_len = 1
        seq_found = False
        remainder = 1
        # longest recurring sequence
        while 1:
            a, remainder = divmod(remainder * 10, divisor)
            if remainder in remainders:
                if seq_found != True:
                    seq_len = i
                    seq_found = True
                if i > (seq_len * 2) + 1:
                    break
                vslice = vysledek[-seq_len:]
                if vslice in seq:
                    if len(vslice) > longest_seq[0]:
                        longest_seq = (len(vslice), divisor, vslice)
                    break
                seq.append(vysledek)
            remainders.append(remainder)
            vysledek += str(a)
            i += 1

        if divisor == 1:
            return longest_seq

        return Problem_26().solution(1, divisor - 1, longest_seq)


if __name__ == "__main__":
    print(Problem_26().solution(1, 999, (1, 1, '')))
