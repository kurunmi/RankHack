def fibon(nums):
    if len(nums) < 3:
        return False
    x = 0
    y = 1
    z = 2

    for _ in range(len(nums) - z):
        if nums[x] + nums[y] == nums[z]:
            return z + 2
        x, y = y, z
        z += 1
    return False


if __name__ == '__main__':
    nums = [0,1,0,2,0,1,0,1,1,2,0,0,0,44,55,0]
    print(fibon(nums))





