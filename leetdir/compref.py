def prefix(strs):
    match = strs[0]
    lt = len(match)
    for i in range(len(strs)):
        while match[:lt] != strs[i][:lt]:
            lt -= 1
    return match[:lt]



if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(strs)
    print(prefix(strs))
