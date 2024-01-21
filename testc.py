def longestConsecutive(nums):
    if not nums: return 0

    # Create a set for faster lookup
    seen = set(nums)

    # Initialize variables for tracking counts
    max_count, count = 0, 1
    num = seen.pop()

    # Iterate through the set
    while seen:
        temp = num
        # Check for consecutive numbers higher than the current number
        while (num + 1) in seen:
            count += 1
            seen.remove(num + 1)
            num = num + 1

        num = temp
        # Check for consecutive numbers lower than the current number
        while (num - 1) in seen:
            count += 1
            seen.remove(num - 1)
            num = num - 1

        # Update the maximum count
        max_count = max(max_count, count)

        # Check if all numbers have been traversed
        if not seen:
            break

        # Move to the next number in the set
        num = seen.pop()
        count = 1

    return max(max_count, count)


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums1 = [0,3,7,2,5,8,4,6,0,1]
    nums2 = [-1,-3,-2,0,1, 200,300, 600,500,100,400]
    nums3 = [-3,-2,1,0,2,4,6,100,200,300,400,500,600]
    nums4 = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
    nums5 = [-8,-4,9,9,4,6,1,-4,-1,6,8]
    nums6 = [0,0,0,0,0]
    print(longestConsecutive(nums3))