# Given an list of strings words, return the first palindromic string in the list. If there is no such string, return an empty string "".
#
# A string is palindromic if it reads the same forward and backward.
#
# Examples
#
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
#
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
#
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

def firstPalindromeInList(lst):
    for element in lst:
        if isPalindrome(element):
            return element
    return ""

def isPalindrome(s):
    # edge case: s is empty
    if len(s) == 0:
        return True
    pointer1 = 0
    pointer2 = len(s) - 1
    while pointer1 < pointer2:
        if s[pointer1] != s[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True

# test isPalindrome function
print(isPalindrome("raceacar"))
print(isPalindrome("racecar"))

# test firstPalindromeInList function
print(firstPalindromeInList(["abc","car","ada","racecar","cool"]))
print(firstPalindromeInList(["notapalindrome","racecar"]))
print(firstPalindromeInList(["def","ghi"]))