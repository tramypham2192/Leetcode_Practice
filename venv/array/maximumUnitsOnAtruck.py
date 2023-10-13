def maximumUnits(boxTypes, truckSize: int) -> int:
    numberOfUnitsPerBoxList = []
    result = 0
    for i in range(len(boxTypes)):
        numberOfUnitsPerBoxList.append(boxTypes[i][1])
    numberOfUnitsPerBoxList.sort(reverse=True)
    print(numberOfUnitsPerBoxList)
    boxTypes.sort(key = lambda x: x[1], reverse=True )
    print(boxTypes)
    for j in range(len(numberOfUnitsPerBoxList)):
        if truckSize < boxTypes[j][0]:
            result += truckSize * boxTypes[j][1]
            break
        if boxTypes[j][1] == numberOfUnitsPerBoxList[j]:
            result += boxTypes[j][1] * boxTypes[j][0]
        truckSize -= boxTypes[j][0]
    return result


print(maximumUnits([[1,3],[2,2],[3,1]], 4))
print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
print(maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]], 35))



