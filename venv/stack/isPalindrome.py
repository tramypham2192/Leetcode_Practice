def isPalindrome(x: int) -> bool:
    # create two empty stacks
    beginningStack = []
    endingStack = []
    # go to the middle of the string(number), append elements into the two stacks
    newString = str(x)
    if len(newString) % 2 == 1:
        for i in range(len(newString) // 2):
            beginningStack.append(newString[i])
        for j in range(len(newString) - 1, len(newString) // 2 , -1):
            endingStack.append(newString[j])
    else:
        for i in range(len(newString) // 2):
            beginningStack.append(newString[i])
        for j in range(len(newString) - 1, len(newString) // 2 - 1, -1):
            endingStack.append(newString[j])
    # compare the pop element from stacks
    for i in range(len(beginningStack)):
        if beginningStack.pop() != endingStack.pop():
            return False
    return True

print(isPalindrome(1001))