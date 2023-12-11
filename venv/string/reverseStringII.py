def reverseString(s, k):
    finalStr = ""
    reversedStr = ""
    # edge case: if len(s) < k
    if len(s) < k:
        for i in range(len(s) - 1, -1, -1):
            finalStr += s[i]
    # happy case
    else:
        divide = len(s) // k
        i = 0
        while len(s) - len(reversedStr) >= k:
            reversedFirst = ""
            first = s[i : i + k]
            for j in range(len(first) - 1, -1, -1):
                reversedFirst += first[j]
            middle = s[i + k : i + 2 * k]
            reversedStr += reversedFirst + middle
            i = i + 2 * k
        if len(s) - len(reversedStr) > 0:
            for m in range(len(s) - 1, len(reversedStr) - 1, -1):
                reversedStr += s[m]
            finalStr = reversedStr
        else:
            finalStr = reversedStr
    return finalStr

# print(reverseString("abcdefgl", 2))
# print(reverseString("abcdefg", 3))
print(reverseString("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))
