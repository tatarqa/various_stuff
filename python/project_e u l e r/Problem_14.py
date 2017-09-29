def collatz_sequence(N):
    out = []
    while N > 1:
        if N % 2 == 0:
            N /= 2
        else:
            N *= 3
            N += 1
        out.append(N)
    yield out


seq_length = longest_nr = 0
for c in range(1, 1000000):
    for item in collatz_sequence(c):
        if len(item) > seq_length:
            seq_length = len(item)
            longest_nr = c

print longest_nr, seq_length
