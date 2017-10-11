def factorize(nr):
    factorial = 1
    while nr > 0:
        factorial *= nr
        nr -= 1

    return factorial


def count_paths(N):
    N *= 2
    if N % 2 == 0:
        part = N / 2
    else:
        part = N / 3
    n = factorize(N)
    r = factorize(part) * factorize(N - part)
    return n / r


def main():
    print count_paths(20)


if __name__ == "__main__":
    main()


#
