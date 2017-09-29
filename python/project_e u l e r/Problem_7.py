primeNumbers = []


def sqrroot():
    yield 2
    for i in range(1000000):
        isPrime = ''
        if not i % 2 == 0 and i > 1:
            for nr in primeNumbers:
                if nr < i / 2:
                    if i % nr == 0 and i not in primeNumbers:
                        isPrime = False
            if i not in primeNumbers and isPrime is not False:
                primeNumbers.append(i)
                yield i


for i, number in enumerate(sqrroot(), start=1):
    if i == 10001:
        print i
        break
