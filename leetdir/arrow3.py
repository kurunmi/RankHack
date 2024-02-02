def brokenArrow(points):
    if not points:
        return 0
    points = sorted(points, key=lambda x: x[1])
    last_arr = float('-inf')
    count = 0
    for first, last in points:
        if first > last_arr:
            count += 1
            last_arr = last
    return count


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(brokenArrow(points1))