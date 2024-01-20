from collections import Counter
def grouAnagrams(strs):
    out = []
    uniq = {}
    out_index = 0
    if len(strs) <= 1:
        out.append(strs)
        return out
    for value in strs:
        mystr = str(sorted(value))
        if mystr not in uniq:
            uniq[mystr] = out_index
            out.append([])
            out_index += 1
        out[uniq[mystr]].append(value)
    return out

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs1 = ["bat"]
    print(grouAnagrams(strs1))




