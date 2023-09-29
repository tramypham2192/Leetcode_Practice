def intersect(nums1, nums2):
    # put all elements of two arrays into two hash tables
    # compare the elements and its frequencies in two hash tables
    # if both conditions are met, add elements into the result array

    dict1 = {}
    dict2 = {}
    resultArray = []
    for i in range(len(nums1)):
        if nums1[i] not in dict1:
            dict1[nums1[i]] = 1
        else:
            dict1[nums1[i]] += 1
    for j in range(len(nums2)):
        if nums2[j] not in dict2:
            dict2[nums2[j]] = 1
        else:
            dict2[nums2[j]] += 1
    print(dict1)
    print(dict2)
    for element in dict1:
        if element in dict2:
            if dict1[element] == dict2[element]:
                if dict1[element] > 1:
                    for k in range(dict1[element]):
                        resultArray.append(element)
                if dict1[element] == 1:
                    resultArray.append(element)
            else:
                if dict1[element] > dict2[element]:
                    for k in range(dict2[element]):
                        resultArray.append(element)
                if dict1[element] < dict2[element]:
                    for k in range(dict1[element]):
                        resultArray.append(element)
    return resultArray

# print(intersect([4, 9, 5], [9,4,9,8,4]))
print(intersect([1], [1]))