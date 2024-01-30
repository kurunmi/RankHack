def brokenArrow(points):
    if not points:
        return 0
    valid_points = []
    valid_points_right = []
    points1 = sorted(points, key=lambda  x:x[1])
    points = sorted(points, key= lambda x:x[0])
    for index in range(len(points)):
        if not valid_points:
            valid_points.append(points[index])
        elif valid_points[-1][0] <= points[index][0] <=  valid_points[-1][1]:
            valid_points[-1] = [max(points[index][0], valid_points[-1][0]),
                                min(points[index][1], valid_points[-1][1])]
        else:
            valid_points.append(points[index])
    for index in range(len(points1)-1, -1, -1):
        if not valid_points_right:
            valid_points_right.append(points1[index])
        if valid_points_right[-1][1] <= points1[index][0] <= valid_points_right[-1][0]:
            valid_points_right[-1] = [max(points1[index][0], valid_points[-1][0]),
                                      min(points1[index][1], valid_points[-1][1])]
        else:
            valid_points_right.append(points1[index])
    return min(len(valid_points), len(valid_points_right))


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(brokenArrow(points1))
