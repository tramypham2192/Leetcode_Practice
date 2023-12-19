def removeDuplicates(nums) -> int:
    if len(nums) == 0:
        return 0
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(nums):
        if nums[pointer2] != nums[pointer1]:
            pointer1 += 1
            nums[pointer1] = nums[pointer2]
        pointer2 += 1
    return pointer1 + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))