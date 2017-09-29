def max_palidromic():
    for i in range(100, 1000):
        for c in range(100, 1000):
            s = str(i * c)
            slen = len(s)
            if s[:slen / 2] == s[slen / 2:][::-1]:
                yield s

highest=0

for nr in max_palidromic():
    if nr > highest:
        highest = nr

print highest