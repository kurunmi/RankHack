def maxPoints(points):
    plen = len(points)
    pdict = {}
    for index in range(plen):
        x,y = points[index]
        for index1 in range(index+1, plen):
            x1 = x - points[index1][0]
            y1 = y - points[index1][1]
            z1 = x1 * y - y1 * x
            pdict[(x1, y1, z1)] = 0
    for x in range(plen):
        a,b = points[x]
        for y in pdict:
            if y[1] * b == y[0] * a + y[2]:
                pdict[y]+= 1
    m = 1
    for a in pdict:
        m = max(m, pdict[a])
    return m



if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    print(maxPoints(myarr))