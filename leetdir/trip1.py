def trip1(nums):
    l = len(nums)-1
    if l < 2:
        return False
    if l == 2:
        return nums[l] > nums[l-1] > nums[l-2]
    for i in range(l-2):
        for j in range(i+1, l-1):
            k = j+1
            while k < l:
                print('checks', i, j, k, nums[i], nums[j], nums[k])
                if nums[i] < nums[j] < nums[k]:
                    print(i, j, k, nums[i], nums[j], nums[k])
                    return True
                k += 1
    return False



if __name__ == '__main__':
    print(trip1([4,3,4,3,3,3,4,3,1,3,3,3,1,2,7]))

