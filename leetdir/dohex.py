def dohex(num):
    hxconv = "0123456789abcdef"

    if num < 0:
        num = (1 << 32) + num
    print(num)

    result = ""
    while num > 0:
        digit = num % 16
        num = num // 16
        result += str(hxconv[digit])
    return result

if __name__ == '__main__':
    num = 65336122812
    num1 = -33
    print(dohex(num1))
