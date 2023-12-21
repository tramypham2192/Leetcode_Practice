# Given a string s, return True if the s can be palindrome after deleting at most one character from it. Otherwise, return False.

# Input: s = "aba"
# Output: True

# Input: s = "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Input: s = "abc"
# Output: False

# def isPalindromeAfterDeletingAtMostOneChar(s):
#     for j in range(len(s)):
#         if isPalindrome(s.replace(s[j], "")):
#             return True
#     return False
# def isPalindrome(s):
#     if len(s) == 0:
#         return True
#     pointer1 = 0
#     pointer2 = len(s) - 1
#     while pointer1 < pointer2:
#         if s[pointer1] != s[pointer2]:
#             return False
#         pointer1 += 1
#         pointer2 -= 1
#     return True

# SOLUTION 2: WITHOUT WRITING HELPER FUNCTION IS PALINDROME
def isPalindromeAfterDeletingAtMostOneChar(s):
    p1=0
    p2=len(s)-1
    while p1<=p2:
        if s[p1]!=s[p2]:
            string1=s[:p1]+s[p1+1:]
            string2=s[:p2]+s[p2+1:]
            return string1==string1[::-1] or string2==string2[::-1]
        p1+=1
        p2-=1
    return True



# test [: : -1] method
# print("abc"[::-1])

# print(isPalindrome("racecar"))
# print(isPalindrome("raceacar"))
# print("abca"[: 2])
print(isPalindromeAfterDeletingAtMostOneChar("abca"))
print(isPalindromeAfterDeletingAtMostOneChar("aba"))
print(isPalindromeAfterDeletingAtMostOneChar("abc"))

