def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewelNumber = 0
    # create two dictionaries
    stoneDict = {}
    jewelDict = {}
    for i in range(len(stones)):
        if stones[i] not in stoneDict:
            stoneDict[stones[i]] = 1
        else:
            stoneDict[stones[i]] += 1
    for j in range(len(jewels)):
        if jewels[j] not in jewelDict:
            jewelDict[jewels[j]] = 1
        else:
            jewelDict[jewels[j]] += 1
    # check if elements in stoneDict is in jewelDict
    for element in stoneDict:
        if element in jewelDict:
            jewelNumber += stoneDict[element]
    # if yes, get the value of that element
    # sum up the values
    return jewelNumber


