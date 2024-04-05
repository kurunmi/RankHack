def candy(ratings):
    size = len(ratings)
    outarr = [1] * size

    for index in range(size-1):
        print(ratings[index], ratings[index+1])
        if ratings[index] < ratings[index + 1]:
            outarr[index + 1 ] = max(outarr[index + 1] , outarr[index] + 1)
    print(outarr)

    for r_index in range(size-2, -1, -1):
        print(ratings[r_index + 1], ratings[r_index])
        if ratings[r_index + 1] < ratings[r_index]:
            outarr[r_index] = max(outarr[r_index] , outarr[r_index + 1] + 1)
    print(outarr)
    return sum(outarr)

if __name__ == '__main__':
    ratings = [1, 0, 2]
    ratings1 = [1,2,2,3,1]
    print(candy(ratings1))

