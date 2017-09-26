def main():
    sum = 0
    sqrsum = 0
    for n in range(1, 101):
        sum += n
        sqrsum += n ** 2

    yield sum ** 2, sqrsum, sum ** 2 - sqrsum


for item in main():
    print item
