def recursion_test(i):
    print(i, "hello world")
    if i > 0:
        recursion_test(i - 1)

recursion_test(5)

def factorial(num):
    if num < 0:
        raise ValueError("num must be greater than zero")
    if num == 0:
        return 1
    num * factorial(num - 1)
print(factorial(0))

def reverse(str):
    if str == '':
        return ''
    return str[-1] + reverse(str[:len(str) - 1])
print(reverse("a"))

print("abcd"[: len("abcd") - 1])

def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)
print(bunny(50))

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(parens[1 : len(parens) - 1])
    else:
        return False

#
# # print("abcd"[1 : len("abcd") - 1])
print(is_nested_parens("(()"))
print(is_nested_parens("(())"))
print(is_nested_parens(""))

def search(array, query):
    if len(array) == 0:
        return False
    elif query in array:
        return True
    else:
        return search(array[: len(array) - 1], query)

print(search(["b", "c", "a"], "a"))
print(search([], "a"))

def is_palindrome(text):
    if len(text) == 0:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1 : len(text) - 1])

print(is_palindrome(""))
print(["b", "c", "a"][:len(["b", "c", "a"]) - 1])
print("abba"[1 : len("abba") - 1])

def digit_match(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num1 % 10 == num2 % 10:
        return 1 + digit_match(num1 // 10, num2 // 10)
    else:
        return digit_match(num1 // 10, num2 // 10)

print(digit_match(1072503891, 62530841))
print(digit_match(234567891, 2345678))