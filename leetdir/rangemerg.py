def merge(intervals):
    if not intervals:
        return intervals
    intervals.sort(key=lambda x: x[0])
    final = []
    for item in intervals:
        if not final or item[0] > final[-1][1]:
            final.append(item)
        else:
            final[-1] = [min(final[-1][0], item[0]), max(final[-1][1], item[1])]
        print(item, final)
    return final



if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals1 = [[1,4],[-4,5]]
    intervals2 = [[1,4],[0,4]]
    intervals3 = [[1,4],[2,3]]
    print(merge(intervals))
