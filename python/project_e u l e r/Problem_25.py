import time


def poor_fib(n):
    if n <= 1:
        return n
    return poor_fib(n - 1) + poor_fib(n - 2)


def fast_fib(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fast_fib(n - 1) + fast_fib(n - 2)
    return memo[n]


def paskvil(n):
    fibonacci = []
    i = 0
    s = 0
    while 1:
        if i <= 2:
            fibnr = i
            fibonacci.append(fibnr)
        else:
            fibnr = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(fibnr)
        if fibnr % 2 == 0:
            s += fibnr
        i += 1
        if i == n:
            return fibnr


def timer(mthd, *args):
    start = time.time()
    done = mthd(*args)
    end = time.time()
    return done, end - start


#

def problem_25(mthd, n):
    i = 0
    while 1:
        if not i <= 1:
            if mthd(i) >= n:
                return i
        i += 1


if __name__ == "__main__":
    print(timer(problem_25, paskvil, 10 ** (1000 - 1)))
    print(timer(problem_25, fast_fib, 10 ** (1000 - 1)))
    # print(timer(problem_25, poor_fib, 10 ** (1000 - 1)))
