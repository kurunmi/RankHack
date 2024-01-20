def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    return len(set(s)) == len(set(t)) == len(set(zip(s,t)))


if __name__ == '__main__':
    s = 'petitep'
    t = 'malelam'
    s1 = "bbbaaaba"
    t1 = "aaabbbba"
    print(isIsomorphic(s, t))