from collections import defaultdict


def maxPoints(points):
    plen = len(points)
    if plen < 2:
        return plen
    mymax = 0
    for i in range(plen):
        slopes = defaultdict(int)
        for j in range(i+1, plen):
            slope = 'inf' if points[i][0] == points[j][0] else (
                    (points[i][1] - points[j][1]) /  (points[i][0] - points[j][0])
                                                                )
            slopes[slope] +=1
        if slopes:
            mymax = max(mymax, max(slopes.values()))
    return mymax + 1




if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    arr2 = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    print(maxPoints(arr1))