#!/usr/bin/python3
import math

romans = {1:    ['I', False],
          5:    ['V',  1],
          10:   ['X',  1],
          50:   ['L',  10],
          100:  ['C',  10],
          500:  ['D',  100],
          1000: ['M',  100]}

dictarr = [1000,500,100,50,10,5,1]

special_cases = ['I', 'C', 'X']

def rome(num):
    output = []
    size = len(dictarr)
    counter = 0
    while counter <= size-1:
        host = dictarr[counter]
        offset = romans[host][1]
        prev_host = dictarr[counter - 1]
        prev_offset = romans[prev_host][1]
        rem = 0
        if num >= host:
            var, rem = math.floor(num/host), num % host
            vararr = [romans[host][0]] * var
            num = rem
            output.extend(vararr)
        if host > num >= host - offset:
            vararr = [romans[offset][0], romans[host][0]]
            output.extend(vararr)
            num -= (host - offset)
        counter += 1
    output = ''.join(output)
    return output


if __name__ == '__main__':
    print(rome(1))


