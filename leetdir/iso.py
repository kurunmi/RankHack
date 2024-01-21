def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for index in range(len(s)):
        if s[index] in s_dict and s_dict[s[index]] != t[index]  or t[index] in t_dict and t_dict[t[index]] != s[index]:
            return False
        s_dict[s[index]] = t[index]
        t_dict[t[index]] = s[index]
    return True


if __name__ == '__main__':
    s = 'petitep'
    t = 'malelam'
    s1 = "bbbaaaba"
    t1 = "aaabbbba"
    print(isIsomorphic(s, t))
