def getrt(x, n):
    if x == 0:
        return x
    if n == -1:
        return 1/x
    elif n == 0:
        return x
    elif n == 1:
        return x
    return  x ** n

if __name__ == '__main__':
    print(getrt(2, -2))




