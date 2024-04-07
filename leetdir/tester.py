def arrtest(arr):
    mytmp = 0
    while arr:
        mytmp += arr.pop(0) -3
        print(mytmp)
    print(mytmp)


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9]
    arrtest(arr)
