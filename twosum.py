#!/usr/bin/python3

def twosum(numbers, target):
    size = len(numbers)
    maxval = target - numbers[0]
    index1 = 0
    index2 = size - 1
    while numbers[index2] > maxval:
        index2 -= 1
    while index2 > index1:
        while numbers[index2] + numbers[index1] < target and index2 > index1:
            print(index2, index1)
            index1 += 1
        if numbers[index2] + numbers[index1] == target:
            print(numbers[index1], numbers[index2])
            return [index1+1, index2+1]
    index2 -= 1


if __name__ == '__main__':
    #numbers = [2, 7, 11, 15]
    #target = 9
    numbers = [-1, 0]
    target = -1
    #numbers = [-5, -2, 1,  2, 3, 5, 7, 11, 33]
    #target = 6
    print(twosum(numbers, target))
