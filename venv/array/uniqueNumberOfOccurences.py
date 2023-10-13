def uniqueOccurrences(arr) -> bool:
    # count the frequency of each element and put into a dictionary
    # if the frequency of one element already in the dict.values() -> return False
    # return True at the end of the for loop
    dict = {}
    for i in range(len(arr)):
        count = 0
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] += 1
    frequencySet = set(dict.values())
    if len(frequencySet) != len(dict.values()):
        return False
    return True
print(uniqueOccurrences([1,2,2,1,1,3]))

