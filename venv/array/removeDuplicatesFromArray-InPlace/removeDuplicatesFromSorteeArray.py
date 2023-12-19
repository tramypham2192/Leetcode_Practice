def removeDuplicates(nums):
    duplicateCount = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplicateCount += 1
        else:
            nums[i - duplicateCount] = nums[i]
    return len(nums) - duplicateCount

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))