def grouAnagrams(strs):
    out = []
    if len(strs) <= 1:
        out.append(strs)
        return out
    lengths = {}
    out_index = 0
    for index in range(len(strs)):
        index_length = len(strs[index])
        if index_length not in lengths:
            lengths[index_length] = {}
            lengths[index_length][strs[index]] = out_index
            out.append([])
            out[out_index].append(strs[index])
            out_index += 1
        else:
            found = False
            for value in lengths[index_length]:
                if Counter(value) == Counter(strs[index]):
                    found = True
                    out[lengths[index_length][value]].append(strs[index])
            if not found:
                lengths[index_length][strs[index]] = out_index
                out.append([])
                out[out_index].append(strs[index])
                out_index += 1
    return out

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs1 = ["bat"]
    print(grouAnagrams(strs))

