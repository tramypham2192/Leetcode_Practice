# Given a sorted (ascending order) list lst and target value x, find if there exists any pair of elements such that their sum is equal to x.
#
# Input: lst = [10, 20, 35, 50, 75, 80],  x = 70
# Output: True
# Explanation: The pair 20 and 50 sum to the target 70.

def pairSum(lst, x):
    pointer1 = 0
    pointer2 = len(lst) - 1
    while pointer1 < pointer2:
        sum = lst[pointer1] + lst[pointer2]
        if sum < x:
            pointer1 += 1
        elif sum > x:
            pointer2 -= 1
        elif sum == x:
            return lst[pointer1] + lst[pointer2] == x
    return False


print(pairSum([10, 20, 35, 50, 75, 80], 70))

def twoSum(nums, target):
  pointer1 = 0
  pointer2 = len(nums) - 1
  nums.sort()
  while pointer1 < pointer2:
    sum = nums[pointer1] + nums[pointer2]
    if sum < target:
      pointer1 += 1
    elif sum > target:
      pointer2 -= 1
    elif sum == target:
      return [pointer1, pointer2]

newArr = [3, 2, 4]
newArr.sort()
print(newArr)
# print(twoSum([4, 5, 32], 9))
print(twoSum([3, 2, 4], 6))