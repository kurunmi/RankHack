def mergeAlternately(word1, word2):
    myarr1 = list(word1)
    myarr2 = list(word2)
    print(myarr1)
    final = ""
    while myarr1 and myarr2:
        final += myarr1.pop(0)
        final += myarr2.pop(0)
    if myarr1:
        final += ''.join(myarr1)
    elif myarr2:
        final += ''.join(myarr2)

    return final


if __name__ == '__main__':
    w1 = 'abcdef'
    w2 = 'ghi'
    print(mergeAlternately(w1, w2))
