def get_divisors_sum(n):
    divisors_sum = 0
    for c in range(1, (n / 2) + 1):
        if n % c == 0:
            divisors_sum += c

    return divisors_sum


def main(r):
    sum = 0
    for i in range(1, r + 1):
        a = get_divisors_sum(i)
        if a != i:
            b = get_divisors_sum(a)
            if b == i:
                sum += i
    return sum


if __name__ == "__main__":
    print main(10000)
