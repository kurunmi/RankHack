def findmatch(points):
    if not points:
        return 0
    matches = {'slope': {}, 'x': {points[0][0]: 0}, 'y':{points[0][1]: 1}}
    vals = [1, 1]
    index = 2
    end = len(points)
    for x in range(1, end):
        if points[x][0] in matches['x']:
            vals[matches['x'][points[x][0]]] += 1
        else:
            matches['x'][points[x][0]] = index
            vals.append(1)
            index += 1
        if points[x][1] in matches['y']:
            vals[matches['y'][points[x][1]]] += 1
        else:
            matches['y'][points[x][1]] = index
            vals.append(1)
            index += 1
        for y in range(x, end):
            if points[0][0] != points[y][0] and points[0][1] != points[y][1]:
                slope = (points[0][0] - points[y][0]) / (points[0][1] - points[y][1])
                if slope not in matches['slope']:
                    matches['slope'][slope] = index
                else:
                    vals[matches['slope'][slope]] += 1
    return max(vals)


if __name__ == '__main__':
    print(findmatch([[2,0], [1,2], [3,0], [2,3], [5,0]]))