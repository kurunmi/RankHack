def ltrcomb(word):
    count = 0
    for index, ltr in enumerate (word):
        tmp_word = ltr
        count += 1
        next = index + 1
        print("Index", len(word), next, index, ltr, count, tmp_word)
        while next < len(word) and ltr == word[next]:
            tmp_word += word[next]
            count +=1
            next += 1
            print(index, next,  count, tmp_word)
    print(count)

if __name__ == '__main__':
    ltrcomb("abccccbcdbbbbbrstuvaaaaaaaaaaaaaaabcdefgggggggggggggggggggghalahalahalahalahalahala")