from leetdir.nuscores import nuscores


def  merge(nums1, m, nums2, n):
    mlen = len(nums1) - 1
    while n and m:
        if nums1[m-1] >= nums2[n-1]:
            nums1[mlen] = nums1[m-1]
            m -= 1
        else:
            nums1[mlen] = nums2[n-1]
            n -= 1
        mlen -= 1
    while n:
        nums1[mlen] = nums2[n-1]
        n -= 1
        mlen -= 1
    return nums1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums3 = [1]
    o = 1
    nums4 = []
    q = 0
    nums5 = [0]
    r = 0
    nums6 = [1]
    s = 1
    print(merge(nums5, r, nums6, s))
