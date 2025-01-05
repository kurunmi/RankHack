import random

def match1(points):
    if len(points) <= 1:
        return 0
    matches = {'x':{}, 'y':{}, 'slope':{}}
    count_arr = []
    index = 0
    point_len = len(points)
    for i in range(point_len):
        cx, cy = points[i]
        if cx not in matches['x']:
            count_arr.append(0)
            matches['x'][cx] = index
            index += 1
        count_arr[matches['x'][cx]] += 1
        if cy not in matches['y']:
            count_arr.append(0)
            matches['y'][cy] = index
            index += 1
        count_arr[matches['y'][cy]] += 1
        for j in range(i, point_len):
            nx, ny = points[j]
            if cx != nx and cy != ny:
                slope = (ny - cy)/  (nx - cx)
                print(points[i], points[j], slope, matches,count_arr)
                if slope not in matches['slope']:
                    count_arr.append(1)
                    matches['slope'][slope] = index
                    index += 1
                count_arr[matches['slope'][slope]] += 1
                print(points[i], points[j], slope, matches, count_arr)
    print(count_arr)
    print(matches)


def pickIndex(w):
    count = len(w) - 1
    mys = sum(w)
    prob = 0
    if len(w) <2:
        print(0)
        return 0
    while not prob:
        index = random.randint(0, count)
        prob = w[index]/ mys
    print(w[index])

if __name__ == '__main__':
    myarr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    arr1 = [[1,1],[2,2],[3,3]]
    w = [1]
    pickIndex(w)
