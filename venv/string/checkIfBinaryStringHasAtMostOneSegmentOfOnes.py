def checkOnesSegment(s: str):
    lst = s.split("0")
    count = 0
    for element in lst:
        if "1" in element:
            count += 1
    if count > 1:
        return False
    return True

print(checkOnesSegment("1000"))
print("1100011".split("0"))
print("1" in "1100011".split("0")[0])
