def matchit(arr):
    matches = {'slope': {}, 'x':{}, 'y':{}}
    values = []
    index = 0
    end = len(arr)
    for i in range(end):
        for j in range(i+1, end):
            [x, y] = arr[j]
            if arr[i][0] != arr[j][0] and arr[i][1] != arr[j][1]:
                slope = (arr[i][0] - arr[j][0])/ (arr[i][1] - arr[j][1])
                if slope and slope not in matches['slope']:
                    matches['slope'][slope] = index
                    values.append(2)
                    index += 1
                else:
                    values[matches['slope'][slope]] += 1
                print(values, slope, arr[i], arr[j])
        print(values, matches, i, arr[i])
    print(matches)




if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    print(matchit(myarr))
