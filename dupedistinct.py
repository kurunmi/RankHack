def removeDuplicates(nums):
    size = len(nums)
    index = 0
    if size <= 2:
        return size

    size = 31
    for i in range(size, 2):
        print(i)



    print(nums[:index])
    return index

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3,3,3,3,3,4,4,4,5,5,5,5,5,6,6]
    print(removeDuplicates(nums))