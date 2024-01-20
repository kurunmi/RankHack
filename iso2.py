def wordPattern(pattern, s):
    t = s.split()
    if len(pattern) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for index in range(len(pattern)):
        if (pattern[index] in s_dict and s_dict[pattern[index]] != t[index] or
                t[index] in t_dict and t_dict[t[index]] != pattern[index]):
            return False
        s_dict[pattern[index]] = t[index]
        t_dict[t[index]] = pattern[index]
    return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    pattern1 = "abba"
    s1 = "dog cat cat fish"
    pattern2 = "aaaa"
    s2 = "dog cat cat dog"
    print(wordPattern(pattern2, s2))