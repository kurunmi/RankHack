def brokenArrow(points):
    if not points:
        return 0
    valid_points = []
    valid_points_right = []
    points1 = sorted(points, key=lambda  x:x[1])
    points = sorted(points, key= lambda x:x[0])
    point_len = len(points)
    for index in range(point_len):
        index1 = point_len - (1 + index)
        if not valid_points:
            valid_points.append(points[index])
        elif valid_points[-1][0] <= points[index][0] <=  valid_points[-1][1]:
            valid_points[-1] = [max(points[index][0], valid_points[-1][0]),
                                min(points[index][1], valid_points[-1][1])]
        else:
            valid_points.append(points[index])
        if not valid_points_right:
            valid_points_right.append(points1[index1])
        elif valid_points_right[-1][1] <= points1[index1][0] <= valid_points_right[-1][0]:
            valid_points_right[-1] = [max(points1[index1][0], valid_points[-1][0]),
                                      min(points1[index1][1], valid_points[-1][1])]
        else:
            valid_points_right.append(points1[index1])
    return min(len(valid_points), len(valid_points_right))


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(brokenArrow(points1))
