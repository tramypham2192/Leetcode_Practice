def isSubsequence(s: str, t: str) -> bool:
    # edge case: s is empty
    if len(s) == 0:
        return True
    # happy case:
    # checkStr = ""
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(s) and pointer2 < len(t):
        # if pointer1 == len(s) - 1:
        #     if s[pointer1] == t[pointer2]:
                # checkStr += s[pointer1]
                # if checkStr == s:
                #     return True
        # else:
        if s[pointer1] == t[pointer2]:
            # checkStr += s[pointer1]
            pointer1 += 1
        pointer2 += 1
    # return False
    return pointer1 == len(s)
print(isSubsequence("abc", "ahbaghdcd"))
print(isSubsequence("acb", "ahbgdcf"))
print(isSubsequence("", "ahbgdc"))