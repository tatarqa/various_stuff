nr = 600851475143


def rozklad(nr):
    d = 2
    while d * d < nr:
        while nr % d == 0:
            yield d
            nr /= d
        d += 1
    if nr > 1:
        yield nr


for nr in rozklad(nr):
    print nr
