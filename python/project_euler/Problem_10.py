def primeCheck(nr):
    prime = False
    if nr > 1 and nr % 2 != 0 or nr == 2:
        prime = True
        for factor in range(3, 1 + int(round(nr ** 0.5)), 2):
            if (nr % factor) == 0:
                prime = False
    return prime


def iter():
    primes_sum = 0
    for i in xrange(1, 1111111111111111111):
        if i > 2000000:
            print primes_sum
            return
        if primeCheck(i) == True:
            primes_sum += i

if __name__ == "__main__":
    iter()
