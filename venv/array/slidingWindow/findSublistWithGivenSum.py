# Given an integer list nums, find a contiguous sublist of size 3 with a given sum in it.

# Input: nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10], target = 15
# Output: [6, 0, 9]

# Input: nums = [0, 5, -7, 1, -2, 7, 6, 1, 4, 1, 10], target = 15
# Output: [4, 1, 10]

# Input: nums = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], target = -3
# Output: []

def findSublistWithGivenSum(lst, target):
    for i in range(len(lst)):
        pointer1 = i
        pointer2 = i + 3
        sumSublist = sum(lst[pointer1 : pointer2])
        if sumSublist == target:
            return lst[pointer1 : pointer2]
    return []
# test sum method
# print(sum([4, 5, 6]))

print(findSublistWithGivenSum([2, 6, 0, 9, 7, 3, 1, 4, 1, 10], 15))
print(findSublistWithGivenSum([0, 5, -7, 1, -2, 7, 6, 1, 4, 1, 10], 15))
print(findSublistWithGivenSum([0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10], -3))