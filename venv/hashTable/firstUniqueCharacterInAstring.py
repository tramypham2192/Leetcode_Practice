def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    # create a dictionary to store character and its frequency
    dict = {}
    index = -1
    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1
    # print(dict)
    for j in dict.keys():
        if dict[j] == 1:
            index = s.index(j)
            return index
    return index

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))