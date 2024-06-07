def findSubString(s, words):
    from collections import defaultdict
    result = []
    wordlen = len(words[0])
    total = len(words)
    allwords = total * wordlen
    mywords = defaultdict(int)

    if total > len(s):
        return result

    for word in words:
        mywords[word] += 1

    for index in range(wordlen):
        print(index, wordlen)
        seen = defaultdict(int)
        count = 0
        window_start = index

        for i in range(index, len(s) - wordlen + 1, wordlen):
            current = s[i:i+wordlen]
            print("c", i, current, current in mywords)
            if current in mywords:
                seen[current] += 1
                count += 1
                while seen[current] > mywords[current]:
                    left = s[window_start:window_start + wordlen]
                    seen[left] -= 1
                    count -= 1
                    window_start += wordlen
                if count == total:
                    print(s[window_start:window_start+allwords])
                    result.append(window_start)
                    left = s[window_start: window_start + wordlen]
                    seen[left] -= 1
                    count -= 1
                    window_start += wordlen
            else:
                seen.clear()
                print("clear", current, window_start, count, i)
                window_start = i + wordlen
                count = 0

    return result






if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    words1 = ["a","a"]
    s1 = "aaa"
    print(findSubString(s1, words1))