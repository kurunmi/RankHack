#!/usr/bin/python3

def reverse(s):
    arr = s.split()
    if len(arr) <= 1:
        return arr
    y = len(arr)-1
    for x in range(len(arr)):
        if x < y:
            tmp = arr[x]
            arr[x] = arr[y]
            arr[y] = tmp
            y -=1
    return " ".join(arr)


if __name__ == '__main__':
    print(reverse(" Boys girls x y y amebo boys"))