#!/usr/bin/python3

def getpairs(arr, k):
    output = []
    start = arr[0]
    end = arr[len(arr) -1]
    last = max(start, end)
    pair_tracker = {}
    arr_tracker = {}
    for x in arr:
        otherx = k - x
        if x <= last  and x > start and otherx <= last and otherx > start:
            pair_tracker[otherx] = x
            if x not in arr_tracker and otherx not in arr_tracker and otherx in pair_tracker and x != otherx:
                pair = [otherx, pair_tracker[otherx]]
                output.append(pair)
                del pair_tracker[otherx]
            arr_tracker[x] = 1
            arr_tracker[otherx] = 1
    return output






if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 123]
    print(getpairs(arr, 99))
