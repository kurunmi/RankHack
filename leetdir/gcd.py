def wgcd(w1, w2):
    if w1 + w2 != w2 + w1:
        return ""

    l1 = len(w1)
    l2 = len(w2)

    while l2:
        print(l1, l2)
        l1, l2 = l2, l1 % l2
    print(l1)
    return w1[-l1:]


if __name__ == '__main__':
    print(wgcd("sss", "sssssssssss"))