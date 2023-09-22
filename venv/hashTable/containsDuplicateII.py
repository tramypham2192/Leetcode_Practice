# trial 1: 1 test case failed among the first 4 test cases

# def containsNearbyDuplicate(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     # create an empty hash table
#     # push elements of arrays into hash table,
#     # if encounter the same element, retrieve the index from
#     # the hash table of the existing element in the hash table
#     # subtract between the indexes and compare with k
#     nonDuplicateElements = {}
#     compareArr = []
#     for i in range(len(nums)):
#         if nums[i] not in nonDuplicateElements:
#             nonDuplicateElements[nums[i]] = i
#         else:
#             compareArr.append(i - nonDuplicateElements[nums[i]])
#     for i in range(len(compareArr)):
#         if compareArr[i] <= k:
#             return True
#     return False

# Trial 2 - 19/56 test cases passed

# def containsNearbyDuplicate(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     # create an empty hash table
#     # push elements of arrays into hash table,
#     # if encounter the same element, retrieve the index from
#     # the hash table of the existing element in the hash table
#     # subtract between the indexes and compare with k
#     nonDuplicateElements = {}
#     compareArr = []
#     for i in range(len(nums)):
#         if nums[i] not in nonDuplicateElements:
#             nonDuplicateElements[nums[i]] = i
#     for j in range(len(nums)):
#         for idx in range(len(nonDuplicateElements.items())):
#             if j > idx and nums[j] == nonDuplicateElements.items()[idx][0]:
#                 if j - nonDuplicateElements.items()[idx][1] <= k:
#                     return True
#     return False

# Solution
def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # create an empty hash table
    # push elements of arrays into hash table,
    # if encounter the same element, retrieve the index from
    # the hash table of the existing element in the hash table
    # subtract between the indexes and compare with k
    nonDuplicateElements = {}
    compareArr = []
    for j in range(len(nums)):
        if nums[j] in nonDuplicateElements:
            if j - nonDuplicateElements[nums[j]] <= k:
                return True
        nonDuplicateElements[nums[j]] = j
    return False

# Optimal solution: not using hash table, but using hash set
print(containsNearbyDuplicate([1,2,3,1], 3))