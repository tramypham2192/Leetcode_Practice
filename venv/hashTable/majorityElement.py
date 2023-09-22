def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # create an empty hash table
    frequencyMap = {}
    # count the frequencies of elements in the array
    count = 0
    for i in range(len(nums)):
        if nums[i] not in frequencyMap:
            frequencyMap[nums[i]] = 1
        else:
            frequencyMap[nums[i]] += 1
    # iterate the hash table's values and return if the frequency of the element > ()len(array) / 2)
    for item in frequencyMap.items():
        if item[1] > (len(nums) / 2):
            return item[0]
print(majorityElement([2,2,1,1,1,2,2]))