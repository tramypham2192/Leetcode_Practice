# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # handle edge case n. == 1:
        if n == 1:
            return 1
        left = 0
        right = n
        while left < right:
            midPoint = left + (right - left) // 2
            if isBadVersion(midPoint) == True:
                right = midPoint
            else:
                left = midPoint + 1
        if left == right and isBadVersion(left) == True:
            return left
        return -1
