def insert(intervals, newInterval):
    result = []
    if not intervals:
        result.append(newInterval)
        return result
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])
    for item in intervals:
        if not result or item[0] > result[-1][1]:
            result.append(item)
        else:
            result[-1] = ([min(item[0], result[-1][0]), max(item[1], result[-1][1])])
    return result



if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    intervals1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval1 = [4, 8]
    intervals2 = [[0,5],[9,12]]
    newInterval2 = [7,16]
    print(insert(intervals2, newInterval2))
