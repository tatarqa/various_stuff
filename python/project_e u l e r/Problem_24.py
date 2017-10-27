def factorize(nr):
    factorial = 1
    while nr > 0:
        factorial *= nr
        nr -= 1

    return factorial


def problem_24(**keywords):
    nthItem = keywords.get('nthItem')
    variants = keywords.get('variants')
    numbers = [nr for nr in range(nthItem)]
    nthItem -= 1  # start from 0
    output = []
    while variants > 0:
        variants -= 1
        allCombinations = factorize(variants)
        division = (nthItem // allCombinations, nthItem % allCombinations)
        output.append(numbers[division[0]])
        del numbers[division[0]]
        nthItem = division[1]
    return ''.join(str(x) for x in output)


def main():
    print problem_24(variants=10, nthItem=10 ** 6)


if __name__ == "__main__":
    main()
