def jump(nums):
    maxjump = 0
    final_dest = len(nums) -1
    current_jump = 0
    jump_count = 0

    if len(nums) < 2:
        return jump_count

    for index in range(0, len(nums)):
        maxjump = max(index + nums[index], maxjump)
        print(jump_count, index, nums[index], maxjump, final_dest)
        if maxjump >= final_dest:
            jump_count += 1
            return jump_count
        if index == current_jump:
            current_jump = maxjump
            jump_count += 1





if __name__ == '__main__':
    nums = [0]
    nums1 = [2,3,0,1,4]
    nums2 = [1,3,1,1,1,4,2,1,1,2,0,0]
    print(jump(nums))