s=int(0)
for i in range(1000):
    if i > 0:
        if i % 3 == 0 or i % 5 == 0:
            s+=i

print s