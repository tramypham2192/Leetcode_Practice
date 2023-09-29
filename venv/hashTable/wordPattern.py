class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # handle case "aba" and "cat cat cat dog"
        if (len(list(pattern))) != len(s.split()):
            return False
        # handle case "abba" and "dog dog dog dog"
        patternSet = set()
        stringSet = set()
        for i in range(len(pattern)):
            if pattern[i] not in patternSet:
                patternSet.add(pattern[i])
        for j in range(len(s.split())):
            if s.split()[j] not in stringSet:
                stringSet.add(s.split()[j])
        if len(patternSet) != len(stringSet):
            return False
        # handle the rest
        if len(patternSet) == len(stringSet):
            # create a hash map
            dict = {}
            # convert string s to be a list
            wordList = s.split()
            # push the pattern character to by key, the sub-string inside s
            # to be value
            # combine the values following the pattern
            # compare the combinedValues with string s
            # if different, return False
            combineWords = ""
            for i in range(len(pattern)):
                if wordList[i] not in dict.values():
                    dict[pattern[i]] = wordList[i]
            for j in range(len(pattern)):
                combineWords += dict[pattern[j]] + " "
            # print(dict)
            # print(combineWords)
            if combineWords.split() != s.split():
                return False
            return True