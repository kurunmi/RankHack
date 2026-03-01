
def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    tot = l1 + l2
    print(tot)
    md = tot // 2
    i1 = i2 = 0
    current = previous = False
    for _ in range(md + 1):
        previous = current
        if i1 < l1 and (i2 >= l2 or nums1[i1] <= nums2[i2]):
            current = nums1[i1]
            i1 += 1
        else:
            current = nums2[i2]
            i2 += 1
    print(current, previous, md)
    if tot % 2 == 0:
        return (current + previous) / 2
    return current


if __name__ == '__main__':
    num1 = [1,3]
    num2 = [2]
    print(findMedianSortedArrays(num1, num2))