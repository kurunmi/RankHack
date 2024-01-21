#!/usr/bin/python3

def repchar(s):
    final = {}
    subst = ""
    for char in s:
        if char not in final:
            subst += char
            final[char] = 0
    print(subst)
    return len(subst)

if __name__ == '__main__':
    s = "abcabcbb"
    t = "bbbbb"
    u = "pwwkew"
    print(repchar(u))