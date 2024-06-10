def merge(nums1, m, nums2, n):
    pointer1 = m-1
    pointer2 = n-1
    pointer3 = m + n -1
    if m == 0:
        return nums2
    while pointer1 >= 0 and pointer2 >= 0:
        print(nums1, nums1[pointer1], nums2[pointer2])
        if nums1[pointer1] >= nums2[pointer2]:
            nums1[pointer3] = nums1[pointer1]
            pointer1 -= 1

        else:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1
        pointer3 -= 1
    return nums1


if __name__ == '__main__':
    nums1 = [1]
    m = 1
    nums2 = [0]
    n = 0
    print(merge(nums1, m, nums2, n))
