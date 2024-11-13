def matchit(arr):
    matches = {'slope':{}, 'x':{}, 'y':{}}
    values = []
    index = 0
    end = len(arr)
    for i in range(end):
        for j in range(i+1, end):
            if arr[i][0] != arr[j][0] and arr[i][1] != arr[j][1]:
                slope = (arr[i][0] - arr[j][0])/ (arr[i][1] - arr[j][1])
                if slope and slope not in matches['slope']:
                    matches['slope'][slope] = [index, {}]
                    print(matches['slope'][slope][1])
                    matches['slope'][slope][1][str(arr[i])] = 1
                    matches['slope'][slope][1][str(arr[j])] = 1
                    values.append(2)
                    index += 1
                else:
                    if (str(arr[j]) not in matches['slope'][slope][1] and
                            str([arr[j][1],arr[j][0]]) not in matches['slope'][slope][1]):
                        values[matches['slope'][slope][0]] += 1
                        matches['slope'][slope][1][str(arr[j])] = 1
    print(values, matches)
    print(matches)




if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    print(matchit(arr1))
