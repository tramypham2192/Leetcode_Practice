def smallerNumbersThanCurrent(nums):
    # create a dictionary, push all elements into the dictionary
    # count the number of elements in the array that is smaller
    # than the dictionary key
    # sum the values of smaller elements and push to the result array

    # sort the array, saved into a new array - sortedArray
    # find the index of the elements in the origional array
    # in the sortedArray
    # do the subtraction
    # push the subtraction result into resultArray

    origionalArray = []
    for i in range(len(nums)):
        origionalArray.append(nums[i])
    print("origional array: ", origionalArray)
    nums.sort()
    print("nums: ", nums)
    sortedArray = nums
    print("sortedArray: ", sortedArray)
    resultArray = []
    for i in range(len(origionalArray)):
        # print(origionalArray[i], ",", sortedArray.index(origionalArray[i]))
        resultArray.append(sortedArray.index(origionalArray[i]))
    return resultArray

print(smallerNumbersThanCurrent([8,1,2,2,3]))
