class Solution:
    def arraySign(self, nums: List[int]) -> int:
        multiplication = 1
        for element in nums:
            multiplication *= element
        if multiplication > 0:
            return 1
        elif multiplication < 0:
            return -1
        else:
            return 0