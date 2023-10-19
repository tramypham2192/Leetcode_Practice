def sumOfThree(num):
    """
    :type num: int
    :rtype: List[int]
    """
    element = num // 3
    if element * 3 == num and element >= 0:
        return [element - 1, element, element + 1]
    else:
        return []

print(sumOfThree(33))