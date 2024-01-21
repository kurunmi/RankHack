def summaryRanges(nums):
    all_ranges = []
    current_range = []
    for index in range(len(nums)):
        if index - 1 < 0:
            current_range.append(str(nums[index]))
            continue
        if nums[index] - nums[index-1] == 1:
            current_range.append(str(nums[index]))
            continue
        if len(current_range) == 1:
            all_ranges.append(str(current_range[0]))
            current_range = [str(nums[index])]
        else:
            all_ranges.append("%s->%s" % (current_range[0], current_range[-1]))
            current_range = [str(nums[index])]
    if len(current_range) == 1:
        all_ranges.append(str(current_range[0]))
    else:
        all_ranges.append("%s->%s" % (current_range[0], current_range[-1]))
    return all_ranges


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7, 8]
    nums1 = [0, 2, 3, 4, 6, 8, 9]
    print(summaryRanges(nums1))

