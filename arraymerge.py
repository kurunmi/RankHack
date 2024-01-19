#!/usr/bin/python3


def arrmerge(nums1, nums2, n, m):
    index1 = n - 1
    index2 = m - 1
    index3 = m + n - 1
    while index1 >= 0 and index2 >= 0:
        if nums1[index1] >= nums2[index2]:
            nums1[index3] = nums1[index1]
            index1 -= 1
        else:
            nums1[index3] = nums2[index2]
            index2 -= 1
        index3 -= 1
    while index2 >= 0:
        nums1[index3] = nums2[index2]
        index2 -= 1
        index3 -= 1
    return nums1





if __name__ == '__main__':
    nums1 = [1, 2, 3, 77, 122, 0, 0, 0, 0]
    n = 5
    nums2 = [ 2, 5, 6, 11]
    m = 4

    print(arrmerge(nums1, nums2, n, m))

