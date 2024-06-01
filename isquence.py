def isSubsequence(s, t):
    size_s = len(s)
    size_t = len(t)
    if size_s > size_t:
        return False
    if size_s == size_t:
        return s == t
    a = b = 0
    while a < size_s and b < size_t:
        if s[a] == t[b]:
            a += 1
            b += 1
        else:
            b += 1
    return a == size_s

if __name__ == '__main__':
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))

