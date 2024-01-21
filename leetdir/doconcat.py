#!/usr/bin/python3
import copy
import time


def doconcat(s, words):
    saved_dict = {}
    indices = []
    wordlen = len(words[0])
    maxlen = len(words) * wordlen
    for word in words:
        if word not in saved_dict:
            saved_dict[word] = 1
        elif word in saved_dict:
            saved_dict[word] += 1
    if len(s) < maxlen:
        return indices
    for index, value in enumerate(s):
        current_substr = s[index:index+maxlen]
        inner_index = 0
        if len(current_substr) >= maxlen:
            word_dict = copy.deepcopy(saved_dict)
            index_end = inner_index + wordlen
            while index_end <= index+maxlen:
                active_word = current_substr[inner_index:index_end]
                if active_word in word_dict and word_dict[active_word] > 0:
                    word_dict[active_word] -= 1
                    if word_dict[active_word] == 0:
                        del(word_dict[active_word])
                inner_index = index_end
                index_end += wordlen
            if len(word_dict) == 0:
                indices.append(index)
    return indices


if __name__ == '__main__':
    s1= "barfoothefoobarman"
    ws = ["foo", "bar"]
    s2 = "barfoofoobarthefoobarman"
    ws2 = ["bar","foo","the"]
    s3 = "wordgoodgoodgoodbestword"
    ws3 = ["word","good","best","word"]
    print(doconcat(s3, ws3))








