def gcdstr(w1, w2):
    if w1 + w2 != w2 + w1:
        return ""

    l1 = len(min(w1, w1))
    l2 = len(max(w1, w2))

    def gcd(l1, l2):
        while l2:
            l1, l2 = l2, l1 % l2
        return l1

    return w2[:gcd(l1, l2)]






