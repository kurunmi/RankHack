#!/usr/bin/python3

def stack(haystack, needle):
    if len(haystack) < len(needle):
        return 0
    need = len(needle)
    hay = len(haystack)
    x = 0
    while x < len(haystack):
        if x + need > hay:
            return 0
        if haystack[x:need+x] == needle:
            return x
        x += 1
    return 0

if __name__ == '__main__':
    needle = "hay"
    haystack = "myhabahayhabahaybah"
    print(stack(haystack, needle))