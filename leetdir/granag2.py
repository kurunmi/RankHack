def groupAnagrams(strs):
    out = []
    uniq = {}
    if len(strs) <= 1:
        out.append(strs)
        return out
    for string in strs:
        s_string = ''.join(sorted(string))
        if s_string not in uniq:
            uniq[s_string] = [string]
        else:
            uniq[s_string].append(string)
    return list(uniq.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs1 = ["bat"]
    print(groupAnagrams(strs))