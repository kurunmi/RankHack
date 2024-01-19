

def twosum(numbers, target):
    size = len(numbers)
    maxval = target - numbers[0]
    print(maxval)
    index1 = 0
    index2 = size - 1
    while index1 < index2:
        val = numbers[index2] + numbers[index1]
        if val == target:
            return [index1 + 1, index2 + 1]
        if val > target:
            index2 -=1
        if val < target:
            index1 += 1


