def isPalindrome(s):
    # edge case:
    if len(s) == 0:
        return True
    newS = ""
    # reverseS = ""
    for i in range(len(s)):
        if s[i].lower().isalnum() == True:
            newS += s[i].lower()
    pointer1 = 0
    pointer2 = len(newS) - 1
    while pointer1 != pointer2:
        if newS[pointer1] != newS[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(""))
print(isPalindrome("n"))
print(isPalindrome("na"))
print(isPalindrome("race a car"))
print(isPalindrome("nice day"))