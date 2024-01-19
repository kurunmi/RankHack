#!/usr/bin/python
import math
import time

def getMid(arr):
    if len(arr) <= 2:
        return arr[0]
    return math.floor(len(arr)/2)

def get_half_array(arr):
    mid = getMid(arr)
    return [arr[0:mid], arr[mid: len(arr)]]

def check_for_half(arr):
    outarr = []
    count = 0
    for item in arr:
        if len(item) >2:
            count += 1
            item = get_half_array(item)
            outarr.append(item[0])
            outarr.append(item[1])
        else:
            outarr.append(item)
    return (count, outarr)

def unmerge(arr):
    newarray = get_half_array(arr)
    count = 1
    while count:
        count, newarray = check_for_half(newarray)
    return newarray


def compare_array(arr):
    if len(arr) < 2:
        return arr
    if arr[0] > arr[1]:
        tmparr = []
        tmparr.append(arr[1])
        tmparr.append(arr[0])
        return tmparr
    return arr

def compare_arrays(array1, array2):
    post_sort_array = []
    while array1 and array2:
        print(array1[0], array2[0])
        if array1[0] <= array2[0]:
            post_sort_array.append(array1.pop(0))
        else:
            post_sort_array.append(array2.pop(0))
    if array1:
        post_sort_array.extend(array1)
    elif array2:
        post_sort_array.extend(array2)
    return post_sort_array

def single_merge(arr):
    print('merg bororororore   oorororororororor    ororororororr', len(arr))
    tmp_array = []
    for x in range(0, len(arr)):
        print(x)
        print('before', arr[x])
        arr[x] = compare_array(arr[x])
        print('after', arr[x])
        if x % 2:
            y = x -1
            print('x', x, arr[x], 'y',y, arr[y])
            inner_array = []
            #time.sleep(1)
            #print(arr[x], arr[y])
            inner_array = compare_arrays(arr[x], arr[y])
            tmp_array.append(inner_array)
    if len(arr) % 2:
            tmp_array.append(arr[-1])

    return tmp_array






if __name__ == '__main__':
    arr1 = [1, 3, 5, 7, 21, 87, 43, 23, 33, 31, 42, 23, 34, 45, 17, 19, 44, 333, 353, 373]
    arr2 = unmerge(arr1)
    print(arr1)
    print(arr2)
    #for i in range (0, len(arr2)):
    #    arr2[i] = compare_array(arr2[i])
    #print(arr2)
    #array1 = [1,2,3,4]
    #array2 = [2,5,6,7]
    #print(array1, array2)
    #new_arr = compare_arrays(array1, array2)
    #print(new_arr)
    merged_arr = single_merge(arr2)
    print(merged_arr)
    merged_arr = single_merge(merged_arr)
    print(merged_arr)
    merged_arr = single_merge(merged_arr)
    print(merged_arr)
    merged_arr = single_merge(merged_arr)
    print(merged_arr)


#    count = 1
#    while count:
#        count, newarr = check_for_half(newarr)
#        print(count, newarr, arr1)