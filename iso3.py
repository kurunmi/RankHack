def wordPattern(pattern, s):
    t = s.split()
    if len(t) != len(pattern):
        return False
    return len(set(t)) == len(set(pattern)) == len(set(zip(t,pattern)))


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    pattern1 = "abba"
    s1 = "dog cat cat fish"
    pattern2 = "aaaa"
    s2 = "dog cat cat dog"
    print(wordPattern(pattern2, s2))