def canJump(nums):
    jmp = nums[0]
    for i in range(1, len(nums)):
        if jmp == 0:
            return False
        jmp -= 1
        jmp = max(nums[i], jmp)
    return True


if __name__ == '__main__':
    nums = [1,3,2,1,0,4]
    print(canJump(nums))

