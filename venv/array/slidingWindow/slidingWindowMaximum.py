# Given a list lst and an integer w, find the maximum for each and every contiguous sublist of size w.
#
# Input: lst = [1, 2, 3, 1, 4, 5],  w = 3
# Output:  3 3 4 5
# Explanation: There are a total of 4 windows of size 3 in the lst input.
#
# Window #1: [1, 2, 3], max = 3
# Window #2: [2, 3, 1], max = 3
# Window #3: [3, 1, 4], max = 4
# Window #4: [1, 4, 5], max = 5

def maximumSlidingWindow(lst, w):
    resultLst = []
    for i in range(len(lst) - w + 1):
        pointer1 = i
        pointer2 = i + w
        maxSubArray = max(lst[i : i + w])
        resultLst.append((maxSubArray))
    return resultLst

print([1, 2, 3, 1, 4, 5][0 : 3])
print(maximumSlidingWindow([1, 2, 3, 1, 4, 5], 3))

