def cdtest(l1, l2):
    while l2:
        print(l1, l2)
        l1, l2 = l2, l1 % l2
    print(l1, l2)


if __name__ == '__main__':
    l1 = "abcdabcdabcd"
    l2 = "abc"
    cdtest(l1, l2)