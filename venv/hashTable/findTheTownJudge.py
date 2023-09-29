def findJudge(n: int, trust) -> int:
    # create a dictionary
    # put first elements of sub-array to be key, second elements to
    # be value
    # iterate through elements of the dictionary,
    # if exists one value different from the rest, return -1
    # else, return that value
    # if len(trust) == 0:
    #     return -1
    # dict = {}
    # for i in range(len(trust)):
    #     dict[trust[i][0]] = trust[i][1]
    # newSet = set()
    # for value in dict.values():
    #     if value not in newSet:
    #         newSet.add(value)
    # if len(newSet) > 1:
    #     return - 1
    # return set[0]

    newSet = set()
    for i in range(len(trust)):
        if trust[i][0] not in newSet: newSet.add(trust[i][0])
    b = 0
    for num in range(1, n + 1):
        if num not in newSet: b = num
    for key in range(1, n + 1):
        if [key, b] not in trust and key != b: return -1
    return b

print(findJudge(2, [[1, 2]]))