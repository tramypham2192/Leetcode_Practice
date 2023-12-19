# USING BRUTE FORCE - Time complexity O(n^2) - Space complexity: O(1)
def maximumSumOfSublistLengthK(nums, k):
    maxSum = 0
    for i in range(len(nums) - k):
        sumSublist = 0
        for element in nums[i : i + k]:
            sumSublist += element
        if maxSum < sumSublist:
            maxSum = sumSublist
    return maxSum

print(maximumSumOfSublistLengthK([1, 4, 6, 7, 2, 1, 1], 3))

# USING SLIDING WINDOW
def maximumSumOfSublistLengthK(nums, k):
    # calculate the sum of the first sublist
    sumSublist = 0
    maxSum = 0
    for i in range(0, k):
        sumSublist += nums[i]
    maxSum = sumSublist
    # calculate sum of other sublists
    for j in range(1, len(nums) - k):
        sumSublist = sumSublist - nums[j - 1] + nums[j + k - 1]
        if maxSum < sumSublist:
            maxSum = sumSublist
    return maxSum

print(maximumSumOfSublistLengthK([1, 4, 6, 7, 2, 1, 1], 3))

# USING QUEUE
