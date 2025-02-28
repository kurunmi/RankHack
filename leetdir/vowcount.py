def vowcount(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vc = 0
    for letter in s[:k]:
        print(letter)
        if letter in vowels:
            vc += 1
    maxv = vc
    for i in range(k, len(s)):
        if k == 1:
            vc = 0
            if s[i-k:i] in vowels:
                vc = 1
                maxv = max(maxv, vc)
        else:
            if s[1+i-k] in vowels and vc:
                vc -= 1
            if s[i] in vowels and vc:
                vc += 1
            maxv = max(maxv, vc)
    return maxv


if __name__ == '__main__':
    print(vowcount("novowels", 1))