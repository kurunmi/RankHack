#!/usr/bin/python3
import time

troughs = []
def getarr(arr):
    current = False
    previous = False
    edge1 = arr[0]
    edge2 = arr[-1]
    in_arr = False
    array_edge1 = arr[0]
    array_edge2 = arr[-1]
    last = False
    trough_start = False
    trough_end =False
    last_move = False
    edgemin =min(arr[0], arr[-1])
    edgemax = max(arr[0], arr[-1])
    index = 0
    isup = False
    while arr:
        previous = current
        current = arr.pop()
        time.sleep(2)
        index += 1
        if not previous:
            previous = current
            current = arr.pop()
            index += 1
            this_move = 'up'
        last_move = this_move
        if index >= 3:
            if current > previous:
                this_move = 'up'
                if current > array_edge1:
                    array_edge1 = current
            if current < previous:
                this_move = 'down'
            print(arr, last_move, this_move, previous, current)
            time.sleep(4)



if __name__ == '__main__':
    arr = [7,3,4,9]
    print(getarr(arr))