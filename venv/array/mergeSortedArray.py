def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1) - 1, -1, -1):
        if nums1[i] == 0:
            nums1[i] = nums2[len(nums1) - 1 - i]
        if len(nums2) - 1 == len(nums1) - 1 - i:
            break
    nums1.sort()
    return nums1

print(merge([1,2,3, 0, 0, 0], 3,[2,5,6], 3))
print(merge([-1,0,0,3,3,3,0,0,0],  6, [1, 2, 2], 3))
print(merge([-1,-1,0,0,0,0], 4, [-1, 0], 2))