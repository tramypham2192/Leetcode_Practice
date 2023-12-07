# def isSubsequence(s: str, t: str) -> bool:
    # case 1: there is an character in s not in t
    # for j in range(len(s)):
    #     if s[j] not in [char for char in t]:
    #         return False
    # case 2:

    # # use string slice in Python
    # # step 1: create a new string with only same characters in s
    # newStr = ""
    # for i in range(len(t)):
    #     if t[i] in [char for char in s]:
    #         newStr += t[i]
    # print("newStr: ", newStr)
    # # step 2: find indexes of the first character of s and push into a list
    # firstCharIndexes = []
    # for i in range(len(newStr)):
    #     if newStr[i] == s[0]:
    #         firstCharIndexes.append(i)
    # print("first char indexed list: ", firstCharIndexes)
    # # step 3: slice string t according to first char index and s.length to find if s exist in t
    # for i in range(len(firstCharIndexes)):
    #     if newStr[firstCharIndexes[i] : len(s)] == s:
    #         print("newStr[firstCharIndexes[i] : len(s)] :", newStr[firstCharIndexes[i] : len(s)])
    #         return True
    # return False

    # convert s to list
    # listS = [char for char in s]
    # # convert t to list
    # listT = [char for char in t]
    # # check if tupleS is a subset of tupleT
    # res = set(listS).issubset(set(listT))
    # return res

    # for c in s:
    #     i = t.find(c)
    #     if i == -1:
    #         return False
    #     else:
    #         t = t[i + 1:]
    # return True

def isSubsequence(s: str, t: str) -> bool:
    checkStr = ""
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(s) and pointer2 < len(t):
        # edge case: s is empty
        if len(s) == 0:
            return True
        if pointer1 == len(s) - 1:
            if s[pointer1] == t[pointer2]:
                checkStr += s[pointer1]
                if checkStr == s:
                    return True
                # else:
                #     return False
            else:
                pointer2 += 1
        # elif pointer2 == len(t) - 1:
        #     return False
        else:
            if s[pointer1] == t[pointer2]:
                checkStr += s[pointer1]
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1
    return False
print(isSubsequence("abc", "ahbaghdcd"))
print(isSubsequence("acb", "ahbgdcf"))
print(isSubsequence("", "ahbgdc"))