def minimumWindow(s, t):
    from collections import defaultdict
    myt = defaultdict(int)
    left_index = 0
    tlen = len(t)
    count = 0
    current = defaultdict(int)
    result = ""

    if len(s) < len(t):
        return result

    for x in t:
        myt[x] += 1
    strlen = len(s)

    for i in range(len(s)):
        status = False
        if s[i] in myt:
            current[s[i]] += 1
            if current[s[i]] <= myt[s[i]]:
                count += 1
        if count == tlen:
            status = True
        while count == tlen:
            if s[left_index] in current:
                current[s[left_index]] -= 1
                if current[s[left_index]] < myt[s[left_index]]:
                    print(s[i], current[s[left_index]], myt[s[left_index]])
                    count -= 1
            print("loop",  count, tlen,  left_index, s[left_index-1:i+1])
            left_index += 1
            print("brk", count, tlen, left_index, s[left_index-1:i + 1])
        if count < tlen and status:
            currlen = len(s[left_index-1: i+1])
            print("len", currlen, strlen, i, s[left_index-1: i+1])
            if currlen < strlen:
                result = s[left_index-1: i+1]
                strlen = currlen
                print("result", result, currlen, strlen)


    return result

if __name__ == '__main__':
    s = "AAADOBECODEBANC"
    t = "ABC"
    print(minimumWindow(s, t))





