def convert_hex(num):
    hexlist = '0123456789abcdef'

    if num < 0:
        num = (1 << 32) + num
    print (num)
    print (bin(num))
    stack = ""
    while num != 0:
        digit = num % 16
        stack += str(hexlist[digit])
        num = num // 16
    print(''.join(list(reversed(stack))))
    stack = "0x" + ''.join(list(reversed(stack)))
    return stack


if __name__ == '__main__':
    num = -4
    print(convert_hex(num))