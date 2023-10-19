def isValid(s: str) -> bool:
    stack1 = []
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for bracket in s:
        if bracket in pairs:
            stack1.append(bracket)
        else:
            if len(stack1) == 0 or bracket != pairs[stack1.pop()]:
                return False
    return len(stack1) == 0

print(isValid("[](){}"))
print(isValid("{[]}"))