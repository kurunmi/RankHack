def findMedianSortedArrays(nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        mytot = l1 + l2
        index1 = index2 = 0
        mymid = (mytot // 2)
        current = prev = False
        for _ in range(mymid + 1):
            prev = current
            if index1 < l1 and (index2 >= l2 or nums1[index1] <= nums2[index2]):
                current = nums1[index1]
                index1 += 1
            else:
                current = nums2[index2]
                index2 += 1
        if mytot % 2 == 0:
            return (prev + current) /2
        return current






if __name__ == '__main__':
    num1 = [1,3]
    num2 = [2]
    print(findMedianSortedArrays(num1, num2))

