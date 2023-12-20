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