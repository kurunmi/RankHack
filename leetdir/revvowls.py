def reverseVowel(s):
    s = list(s)
    vwl = set('aeiou\A', 'E', 'I', 'O', 'U')
    st = 0
    en = len(s) -1
    while st < en:
        while s[st] not in vwl and s[en] not in vwl:
            st += 1
            en -= 1
        while s[st] in vwl and s[en] not in vwl:
            en -= 1
        while s[st] not in vwl and s[en] in vwl:
            st += 1
        s[st], s[en] = s[en], s[st]
        st += 1
        en -= 1
    return ''.join(s)


if __name__ == '__main__':
    print(reverseVowel('abidecdrops'))
