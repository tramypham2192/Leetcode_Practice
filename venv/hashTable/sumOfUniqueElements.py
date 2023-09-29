class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # create a set
        # if the array element not in set, add it to the set
        dict = {}
        sum = 0
        for element in nums:
            if element not in dict:
                dict[element] = 1
            else:
                dict[element] += 1
        for setElement in dict:
            if dict[setElement] == 1:
                sum += setElement
        return sum
