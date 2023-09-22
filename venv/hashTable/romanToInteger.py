def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    # create a dictionary matching symbol and value
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # go from right to left of the string
    # to check if the previous symbol's matching value
    # smaller or larger than the later symbol
    # 1) if smaller: minus
    # 2) if larger: add
    result = dict[s[len(s) - 1]]
    for i in range(len(s) - 1, 0, -1):
        if dict[s[i - 1]] < dict[s[i]]:
            result -= dict[s[i - 1]]
        else:
            result += dict[s[i - 1]]
    return result

print(romanToInt("LVIII"))

