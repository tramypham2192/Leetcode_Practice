def isAnagram(self, s: str, t: str) -> bool:
    # put all letters in the strings into dictionaries
        dictS = {}
        dictT = {}
        result = True
        if len(s) != len(t):
            result = False
        for i in range(len(s)):
            if s[i] not in dictS:
                dictS[s[i]] = 1
            else:
                dictS[s[i]] += 1
        for j in range(len(t)):
            if t[j] not in dictT:
                dictT[t[j]] = 1
            else:
                dictT[t[j]] += 1
        for letter in dictS:
            if letter not in dictT or dictS[letter] != dictT[letter]:
                result = False
        return result