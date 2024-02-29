def gen_fibon(val):
    num1 = 0
    num2 = 1
    num3 = num2

    if val ==0:
        return 0
    #if val == 1:
    #    return num1
    while num3 < val:
        num1, num2 = num2, num3
        num3 = num1 + num2
    print(num2, num3)
    return min(num3-val, val-num2)


if __name__ == '__main__':
    print(gen_fibon(15))

