oklist = []
sourcelist = []


def main():
    initial_number = 1
    for n in range(1, 21):
        initial_number *= n
    sourcelist.append(initial_number)
    a = 1
    while a:
        for n in sourcelist:
            a = isok_provider(n)
            print n


def isok_provider(nr):
    for n in range(1, 21):
        isok(nr / n)


def isok(nr):
    for n in range(1, 21):
        if nr % n != 0:
            return
    if nr in oklist:
        return False
    sourcelist.append(nr)
    oklist.append(nr)


main()