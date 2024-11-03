def isPal(x):
    if (x % 10 == 0 and x !=0) or x < 0:
        return False
    revertedNumer = 0
    while x > revertedNumer:
        revertedNumer = revertedNumer * 10 + x % 10
        x //= 10
    print(x, revertedNumer, revertedNumer // 10)
    return (x == revertedNumer or x == revertedNumer // 10)




if __name__ == '__main__':
    print(isPal(10))