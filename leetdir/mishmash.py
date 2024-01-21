#!/usr/bin/python3

def mish(strs):
    if not strs:
        return ""
    match = strs[0]
    for i in range(len(strs)):
        val = strs[i]
        matchlen = len(match)
        while match and val[:matchlen] != match:
            match = match[:-1]
            matchlen = len(match)
        print(match, val)
    return match


if __name__ == '__main__':
    print(mish(["abab","aba",""]))