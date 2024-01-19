#!/usr/bin/python3
def get_uniq(mydict):
    for rec in mydict:
        if mydict[rec] == 1:
            return rec

def lonelyinteget(arr):
    numbers = {}
    for num in arr:
        if num not in numbers:
            numbers[num] = 0
        numbers[num] += 1
    unique_num = get_uniq(numbers)
    return unique_num

if __name__ == '__main__':
    arr = [1,2,3,4,3,2,1]
    a = loneluint(arr)
    print(a)
