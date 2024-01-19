#!/usr/bin/python3

def repchar(s):
    currstr = ""
    laststr = ""
    collector = {}
    for char in s:
        if char not in collector:
            currstr += char
            collector[char] = 0
        elif char in collector:
            collector = {}
            if len(currstr) > len(laststr):
                laststr = currstr
            for x, y in enumerate(currstr):
                if y == char:
                    currstr = currstr[x+1:]
                    for record in currstr:
                        collector[record] = 0
            currstr += char
            collector[char] = 0
    print(currstr, laststr )
    return max(len(laststr), len(currstr))


if __name__ == '__main__':
    s = "abcabcbb"
    t = "bbbbb"
    u = "pwwkew"
    g = "eki3ndayo ala4baraba akki5ii"
    print(repchar(g))