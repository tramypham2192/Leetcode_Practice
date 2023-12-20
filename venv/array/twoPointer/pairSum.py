# Given a sorted (ascending order) list lst and target value x, find if there exists any pair of elements such that their sum is equal to x.
#
# Input: lst = [10, 20, 35, 50, 75, 80],  x = 70
# Output: True
# Explanation: The pair 20 and 50 sum to the target 70.

# def pairSum(lst, x):
#     pointer1 = 0
#     pointer2 = len(lst) - 1
#     while pointer1 < pointer2:
#         sum = lst[pointer1] + lst[pointer2]
#         if sum < x:
#             pointer1 += 1
#         elif sum > x:
#             pointer2 -= 1
#         elif sum == x:
#             return lst[pointer1] + lst[pointer2] == x
#     return False
#
#
# print(pairSum([10, 20, 35, 50, 75, 80], 70))

def twoSum(nums, target):
    result = []
    pointer1 = 0
    pointer2 = len(nums) - 1
    # this creates shallow copy, then sort newArr also mean sort nums
    # newArr = nums
    # newArr.sort()
    # while pointer1 < pointer2:
    #     sum = newArr[pointer1] + newArr[pointer2]
        # this creates deep copy -> have to use this way
    newArr = nums.copy()
    newArr.sort()
    while pointer1 < pointer2:
        sum = newArr[pointer1] + newArr[pointer2]
        if sum < target:
            pointer1 += 1
        elif sum > target:
            pointer2 -= 1
        elif sum == target:
            print(nums)
            print(newArr)
            for i in range(len(nums)):
                if nums[i] == newArr[pointer1]:
                    result.append(i)
            for j in range(len(nums)):
                if nums[j] == newArr[pointer2] and j not in result:  # need j not in result for test case [3, 3]
                    result.append(j)
            return result

# test shallow coppy or deep copy
# arr1 = [1, 2, 4]
# arr2 = arr1
# arr2.append(10)
# print(arr1)

# test sort() method
# newArr = [3, 2, 4]
# newArr.sort()
# print(newArr)

# test cases
# print(twoSum([4, 5, 32], 9))
# print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
print(twoSum([3, 2, 3], 6))

