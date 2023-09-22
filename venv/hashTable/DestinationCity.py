def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    resultString = ""
    # create a set to store start elements
    startElementsSet = set()
    for i in range(len(paths)):
        startElementsSet.add(paths[i][0])
    # create a set to store ending elements
    endingElementsSet = set()
    for i in range(len(paths)):
        if paths[i][1] not in startElementsSet:
            resultString = paths[i][1]
    return resultString
print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
