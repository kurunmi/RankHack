def listMerge(nums1, m, nums2, n):
    index1 = m - 1
    index2 = n - 1
    index3 = m + n -1
    while index1 >= 0 and index2 >= 0:
        if nums2[index2] > nums1[index1]:
            nums1[index3] = nums2[index2]
            index2 -= 1
        else:
            nums1[index3] = nums1[index1]
            index1 -= 1
        index3 -= 1
    while index2 >= 0:
        nums1[index3] = nums2[index2]
    return nums1






if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(listMerge(nums1, m, nums2, n))

        




