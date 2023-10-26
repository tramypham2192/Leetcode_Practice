def pivotIndex(nums):
    sumLeft = 0
    sumRight = 0
    for i in range(len(nums) - 1):
        pivotIndex = i
        if i == 0:
            sumLeft = 0
        else:
            sumLeft += nums[pivotIndex - 1]
        sumRight += nums[pivotIndex + 1]
        if sumLeft == sumRight:
            return pivotIndex
    return -1

print(pivotIndex([1,7,3,6,5,6]))