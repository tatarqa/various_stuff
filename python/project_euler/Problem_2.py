
fibonacci=[]
fibnr=0
i=0
s=0
while 1:
    if i <= 2:
        fibnr= i
        fibonacci.append(fibnr)
    else:
        fibnr=fibonacci[i-1]+fibonacci[i-2]
        if fibnr > 4000000:
            break
        fibonacci.append(fibnr)
    if fibnr % 2 == 0:
        s+=fibnr
    i+=1

print s