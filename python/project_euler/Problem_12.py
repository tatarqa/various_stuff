def solve(N):
    x = 0
    for c in xrange(1, N):
        x += c
        row = [x, 1]
        if x % 2 != 0:
            for factor in range(3, 1 + int(round(x ** 0.75)), 2):
                if x % factor == 0:
                    zbytek = x / factor
                    if not factor in row:
                        row.append(factor)

                    if not zbytek in row:
                        row.append(zbytek)

        else:
            for factor in range(2, 1 + int(round(x ** 0.75)), 1):
                if x % factor == 0:
                    zbytek = x / factor
                    if not factor in row:
                        row.append(factor)
                    if not zbytek in row:
                        row.append(zbytek)

        yield row


def main():
    N = 999999999999
    for row in solve(N):
        if len(row) > 500:
            print row
            return


if __name__ == "__main__":
    main()
