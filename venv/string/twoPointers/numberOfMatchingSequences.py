def numMatchingSubseq(s , words) -> int:
    countMatching = 0
    for word in words:
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(word) and pointer2 < len(s):
            if word[pointer1] == s[pointer2]:
                pointer1 += 1
            pointer2 += 1
        if pointer1 == len(word):
            countMatching += 1
    return countMatching