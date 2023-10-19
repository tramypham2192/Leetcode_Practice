def isPalindrome(s):
    arr = list([char.lower() for char in s if char.isalpha() or char.isnumeric()])
    left = 0
    right = len(arr) - 1
    while (left < right):
        if arr[left].lower() != arr[right].lower():
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
