def needlestack(haystack, needle):
    if len(needle) > len(haystack):
        return  -1
    nedlen = len(needle)
    for index in range(len(haystack)):
        if haystack[index] == needle[0]:
            inner, offset = 0, index
            while inner < nedlen and needle[inner] == haystack[offset + inner]:
                print(needle[inner], haystack[offset + inner], inner, offset+inner)
                inner += 1
            print("inner", inner, nedlen)
            if inner == nedlen:
                return offset
    return -1

if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    haystack = "leetcode"
    needle = "leeto"
    print(needlestack(haystack, needle))

