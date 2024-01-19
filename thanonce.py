#!/usr/bin/python3

def thanonce(num):
    val = num.pop()
    count = 1
    for item in num:
        if item == val:
            count += 1
        else:
            count -= 1
            if count == 0:
                val = item
                count = 1
    return val

if __name__ == '__main__':
    print(thanonce([2,2,1,1,1,2,2]))

    print((7 + 13) % 20)
