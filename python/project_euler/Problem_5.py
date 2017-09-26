oklist=[]
sourcelist=[]

def main():
    d = 1
    for c in range(1, 21):
        d *= c
    sourcelist.append(d)


    a = 1
    while a:
        for item in sourcelist:
            a = isok(item)
            print item


def isok(nr):
    for n in range(1, 21):
        checkRange(nr/n)


def checkRange(nr):
    for n in range(1, 21):
        if nr % n != 0:
            return
    if nr in oklist:
        return False
    sourcelist.append(nr)
    oklist.append(nr)

main()



