def groupAnagrams(strs):
    # create a dictionary, the key is a set, the value is a list of strs' elements that have all characters in the set
    # put the elements of the list in a set:
    # if there is one character of the element not in the set -> create a new set, add this set into the dictionary
    # else if all characters of the element is in the set -> add this element into the list  (this list is the key's value in the dictionary)

    dict = {}
    charlist = []
    result = []
    for el in strs:
        charlist.append(tuple(sorted(el)))
    # print(charlist)
    for i in range(len(charlist)):
        sameChar = []
        if charlist[i] not in dict:
            sameChar.append((strs[i]))
            dict[charlist[i]] = sameChar
        else:
            dict[charlist[i]].append(strs[i])
    for el in dict.values():
        result.append(el)
    return result

print(groupAnagrams(["eat", "foo", "bar", "ate"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))

#shorter version (optimize code):
def groupAnagrams(strs):
    # create a dictionary, the key is a set, the value is a list of strs' elements that have all characters in the set
    # put the elements of the list in a set:
    # if there is one character of the element not in the set -> create a new set, add this set into the dictionary
    # else if all characters of the element is in the set -> add this element into the list  (this list is the key's value in the dictionary)

    dict = {}
    charlist = []
    # result = []
    for el in strs:
        charlist.append(tuple(sorted(el)))
    # print(charlist)
    for i in range(len(charlist)):
        sameChar = []
        if charlist[i] not in dict:
            sameChar.append((strs[i]))
            dict[charlist[i]] = sameChar
        else:
            dict[charlist[i]].append(strs[i])
    # for el in dict.values():
    #     result.append(el)
    return list(dict.values())

#shortest version
# use ''.join(sorted(string)) instead of creating tuple










