def votalgo(nums):
    count = 0
    val = False
    for num in nums:
        if count == 0:
            val = num
            count +=1
        elif val == num:
            count += 1
        else:
            count -= 1
    return val


if __name__ == '__main__':
    nums = [1,2,3,5,5,5,5,5,5,5,5,54,4,4,4]
    print(votalgo(nums))