def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    tot = l1 + l2
    i1 = i2 = 0
    md = tot // 2
    prev = curr = False
    for _ in range(md + 1):
        prev = curr
        if i1 < l1 and (i2 >= l2 or nums1[i1] <= nums2[i2]):
            curr = nums1[i1]
            i1 += 1
        else:
            curr = nums2[i2]
            i2 += 1
    if tot //2 == 0:
        return (curr + prev) / 2
    return curr


if __name__ == '__main__':
    num1 = [1,3]
    num2 = [2]
    print(findMedianSortedArrays(num1, num2))