#!/usr/bin/python3.6


def findblocks(arr):
    k = len(arr)
    left = 0
    left_max = left
    left_bucket = 0
    right = k-1
    right_max = right
    right_bucket = 0
    total = 0

    while left < right:
        left += 1
        right -= 1
        if arr[left] > arr[left_max]:
            left_max = left
            total += left_bucket
            left_bucket = 0
        if arr[left] < arr[left_max]:
            left_bucket += (arr[left_max] - arr[left])
        if arr[right] > arr[right_max]:
            right_max = right
            total += right_bucket
            right_bucket = 0
        if arr[right] < arr[right_max]:
            right_bucket += (right_max - arr[right])

    bucket = 0
    if arr[right_max] >= arr[left_max]:
        left = left_max
        while left != right_max:
            left += 1
            if arr[left] < arr[left_max]:
                bucket += arr[left_max] - arr[left]
            if arr[left] > arr[left_max]:
                left_max = left
                total += bucket
                bucket = 0

    if arr[left_max] > arr[right_max]:
        right = right_max
        while right != left_max:
            right -= 1
            if arr[right] < arr[right_max]:
                bucket += arr[left_max] - arr[left]
            if arr[right] > arr[right_max]:
                right_max = right
                total += bucket
                bucket = 0

    return total



if __name__ == '__main__':
    arr = [7,3,4,9]
    print(findblocks(arr))












