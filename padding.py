#!/usr/bin/python3
import math
import time

def padding(words, maxWidth):
    allwords = ' '.join(words)
    w = 0
    stride = 0
    new_word = []
    wordarr = []
    newarr = []
    row_end = maxWidth
    word_start = -1
    word_end = 0
    wordlen = 0
    chars = 0
    charlen = 0
    while w <= len(allwords)-1:
        if allwords[w] != " ":
            chars += 1
        if allwords[w] != " " and word_start == -1:
            word_start = w
        wordlen += 1
        if w == len(allwords) -1:
            word_end = w+1
            new_word.append(allwords[word_start:word_end])
            word_start = -1
        if (allwords[w] == " " or w == len(allwords)-1) and word_start != -1:
            word_end = w
            charlen += word_end - word_start
            new_word.append(allwords[word_start:word_end])
            word_start = -1
        if stride == maxWidth  :
            w = word_end
            stride = 0
            word_start = -1
            wordarr.append(new_word)
            gaps = len(new_word) -1
            spaces = maxWidth - charlen
            rem = spaces % gaps
            div = math.floor(spaces / gaps)
            print(rem, div)
            for each in new_word:
                if rem:
                    print(each)
                    each += " "
                    rem -= 1
                    print(each)
            thisword = (div * " ").join(new_word)
            newarr.append(thisword)
            print(thisword)
            new_word = []
            chars = 0
            print("lt", wordlen, charlen, spaces, gaps, rem, div)
            charlen =0
        #time.sleep(1)
        print(w, stride, allwords[w], new_word, wordarr, newarr, word_start, word_end, wordlen, len(allwords), chars, charlen)
        w += 1
        stride += 1

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxwWidth = 16
    padding(words, maxwWidth)