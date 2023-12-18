# Given a string str and a target substring sub, write a function that prints all occurrences of the substring sub in the string str. You may assume that the length of the string str is greater than the substring sub.
#
# Input: str = "catdogcatdog"
#        sub = "dog"
# Output:
# Found Substring at Index 3
# Found Substring at Index 9

def allOccurencesOfSubstring(s, w):
    # create an index list which stores the result
    indexLst = []
    for i in range(len(s) - 3 + 1):
        pointer1 = i
        pointer2 = i + 3
        if s[i : i + 3] == w:
            indexLst.append(i)
    return indexLst

print("catdogcatdog"[8 : 11])
print(allOccurencesOfSubstring("catdogcatdog", "dog"))
