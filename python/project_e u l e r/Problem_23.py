def proper_divisors(n):
    i = 2.
    yield 1
    while i <= (n ** 0.5):
        if n % i == 0:
            yield i
            if i != (n / i):
                yield n / i
        i += 1


def number_type(n):
    sum = 0
    for divisor in proper_divisors(n):
        sum += divisor
    if sum > n:
        return 'abundant'
    elif sum == n:
        return 'perfect'
    else:
        return 'deficient'


def get_abundant_nrs(r):
    for n in range(1, r + 1):
        if number_type(n) == 'abundant':
            yield n


def problem_sum(r):
    abundant_nrs = [nr for nr in get_abundant_nrs(r + 1)]
    sum = 0
    for i in range(1, r + 1):
        ok = True
        for nr in abundant_nrs:
            val = i - nr
            if val >= 12:
                if val in abundant_nrs:
                    ok = False
                    break
            else:
                break
        if ok is True:
            sum += i
    return sum


if __name__ == "__main__":
    print problem_sum(28123)
