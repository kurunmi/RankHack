def gcd(w1, w2):
    while w2:
        w1, w2 = w2, w1 % w2
    return w1
