def matchit(points):
    matches = {'slope':{}, 'x':{}, 'y':{}, 'xy':{}}
    values = []
    index = 0
    end = len(points)
    for i in range(end):
        if points[i][0] not in matches['x']:
            values.append(0)
            matches['x'][points[i][0]] = index
            index += 1
        values[matches['x'][points[i][0]]] += 1
        if points[i][1] not in matches['y']:
            values.append(0)
            matches['y'][points[i][1]] = index
            index += 1
        values[matches['y'][points[i][1]]] += 1
        if points[i][0] == points[i][1]:
            if not matches['xy']:
                values.append(0)
                matches['xy'] = index
                index += 1
            values[matches['xy']] += 1
        for j in range(i+1, end):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1] and points[i][0]:
                slope = (points[i][0] - points[j][0])/ (points[i][1] - points[j][1])
                if slope and slope not in matches['slope']:
                    matches['slope'][slope] = {}
                    if str(points[i]) not in  matches['slope'][slope]:
                        matches['slope'][slope][str(points[i])] = [index, {}]
                    matches['slope'][slope][str(points[i])][1][str(points[i])] = 1
                    matches['slope'][slope][str(points[i])][1][str(points[j])] = 1
                    values.append(2)
                    index += 1
                else:
                    if str(points[j]) not in matches['slope'][slope][1]:
                        values[matches['slope'][slope][0]] += 1
                        matches['slope'][slope][1][str(points[j])] = 1
    return  max(values)




if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    arr2 = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    print(matchit(arr2))
