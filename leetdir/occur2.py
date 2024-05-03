def hayneedle(haystack, needle):
    hay = len(haystack)
    need = len(needle)
    index = 0
    if hay < need:
        return -1
    while index < hay:
        if hay - index < need:
            return -1
        if haystack[index:index + need] == needle:
            return index
        index += 1
    return -1

if __name__ == '__main__':
    haystack1 = "sadbutsad"
    needle1 = "sad"
    haystack = "leetcode"
    needle = "leeto"
    haystack2 = "a"
    needle2 = "a"
    print(hayneedle(haystack2, needle2))

