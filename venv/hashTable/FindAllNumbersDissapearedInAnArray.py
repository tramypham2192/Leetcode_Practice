def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    d = {}
    for i in range(len(nums)):
        count = 0
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1
    print(d)
    temp = []
    for i in range(1, len(nums) + 1):
        if i not in d:
            temp.append(i)
    return temp

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))


