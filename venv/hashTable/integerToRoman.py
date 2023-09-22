def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    # create a dict to match symbol with value
    dict = {1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"}
    romanString = ""
    # create a dict with the len
    length_dict = {4: 1000, 3: 100, 2: 10, 1: 1}
    # step 1: break the number into single numbers
    arr = []
    for i in range(len(str(num)), -1, -1):
        if i in length_dict:
            num // length_dict[i]
            arr.append(num // length_dict[i])
            num = num - arr[len(arr) - 1] * length_dict[i]
    # step 2: reverse the arr
    arr.reverse()
    print("arr: ", arr)
    # multiply each element inside arr with 1, 10, 100, 1000
    reverse_arr = []
    for j in range(len(arr) - 1, -1, -1):
        arr[j] * length_dict[j + 1]
        reverse_arr.append(arr[j] * length_dict[j + 1])
    print("reverse_arr: ", reverse_arr)
    # step 3: convert the elements of the reverse_arr to letters
    # for element in reverse_arr:
    #     if element in length_dict:
    #         print(element, " is inside")
    #         # romanString += length_dict[element]
    # return romanString
    for k in reverse_arr:
        if k < 4000:
            romanString += k // 1000 * dict[1000]
        if k == 900:
            romanString = dict[500] + dict[400]
        if k > 500 and k < 900:
            romanString += dict[500] + [(k - 500) // 100] * dict[100]
        if k == 400:
            romanString = dict[400]
        if k > 100 and k < 400:
            romanString += [(k - 100) // 100] * dict[100]
        if k == 100:
            romanString += dict[100]
        if k == 90:
            romanString += dict[90]
        if k > 50 and k < 90:
            romanString += dict[50] + [(k - 50) // 10] * dict[10]
        if k == 40:
            romanString += dict[40]
        if k > 10 and k < 40:
            romanString += [(k - 10) // 10] * dict[10]
        if k == 10:
            romanString += dict[10]
        if k == 9:
            romanString +=  dict[9]
        if k > 5 and k < 9:
            romanString += dict[5] + [(k - 5)] * dict[1]
        if k == 5:
            romanString += dict[5]
        if k > 1 and k < 5:
            romanString += (k // 1) * dict[1]
        if k == 1:
            romanString += dict[1]
    return romanString

# MCMXCIV
# print(1 * len(str(1994)))
print(intToRoman(3999))


# 1st iteration of the loop: 1994 // (1 [len(str(num)) - 1] 000]
# 1994 // 1000
# 994 // 100
# 94 // 10
# 4 // 1