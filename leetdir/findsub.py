#!/usr/bin/python3

def findsub(s, words):
    indices = []
    worddict = get_word_dict(words)
    strlen = len(words) * len(words[0])
    for i in range(len(s) + strlen):
        if s[i:i+strlen] in worddict:
            indices.append(i)
    return indices


def get_word_dict(words):
    lst =[[[] for _ in words] for _ in words]
    word_arr = lst
    intval = 0
    for word in words:
        step = intval
        for i in range (len(word_arr)):
            word_arr[i][step] = word
            step += 1
            if step == len(word_arr):
                step = 0
        intval += 1
    outarr = {}
    for arr in word_arr:
        if arr:
            mystr = ''.join(arr)
            if mystr:
                outarr[mystr] = ''
    return outarr







if __name__ == '__main__':
    print(findsub("barfoofoobarthefoobarman",["foo", "bar", "the"] ))