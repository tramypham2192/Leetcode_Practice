class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            midPoint = left + (right - left) // 2
            if nums[midPoint] == target:
                return midPoint
            elif nums[midPoint] < target:
                left = midPoint + 1
            elif nums[midPoint] > target:
                right = midPoint - 1
        if left == right and nums[left] == target:
            return left
        return - 1