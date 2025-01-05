def hindex(citations):
    citations = sorted(citations, reverse=True)
    myl = len(citations)
    count = 0
    for x in range(myl):
        if citations[x] <= count:
            return count
        count += 1


if __name__ == '__main__':
    citations = [1,2,3,5,5,5,4,5,6]
    print(hindex(citations))