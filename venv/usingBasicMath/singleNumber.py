def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    singleElement = nums[0]
    # sort the array
    nums.sort()
    for i in range(len(nums)):
        # handle the test case which the array has the last element to be the unique element
        if i == len(nums) - 1:
            # compare the elements standing next to each other
            if nums[i] != nums[i - 1]:
                singleElement = nums[i]
        # handle the test case which the array does not have the last element to be the unique element
        else:
            # compare the elements standing next to each other
            if (nums[i] != nums[i - 1] and nums[i] != nums[i + 1]):
                singleElement = nums[i]
    return singleElement

print(singleNumber([0, 0, 1, 1, 2, 2, 3]))

print(len([0, 0, 1, 1, 2, 2, 3]))