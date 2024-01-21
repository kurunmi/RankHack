def isAnagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    s1 = "rat"
    t1 = "car"
    print(isAnagram(s1,t1))
