def factorize(nr):
    factorial = 1
    while nr > 0:
        factorial *= nr
        nr -= 1

    return factorial


def count_paths(N):
    n = factorize(N * 2)
    r = factorize(N) ** 2
    return n / r


def main():
    print count_paths(20)


if __name__ == "__main__":
    main()


#
