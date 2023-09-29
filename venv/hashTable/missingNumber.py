def missingNumber(nums):
    # create a set to put all elements
    # into the set
    newSet = set()
    for i in range(len(nums)):
        if nums[i] not in newSet:
            newSet.add(nums[i])

    # iterate the dictionary keys and compare with
    # element list from 0 -> n to find the missing element
    nums.sort()
    for i in range(len(nums) + 1):
        if i not in newSet:
            return i
    return -1

print(missingNumber([3, 0, 1]))