def hfact(citations):
    citations = sorted(citations, reverse=True)
    count = 0
    while count < len(citations) and count < citations[count]:
        count += 1
    return count



if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    citations1 = [0, 0, 0, 0, 0, 0]
    citations2 = [1,3,1]
    cit3 = [0]
    cit4 = [4,4,0,0]
    cit5 = [24, 24, 24, 24]
    print(hfact(cit4))
