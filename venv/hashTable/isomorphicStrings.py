def isIsomorphic(s, t):
    map1 = []
    map2 = []
    for characterS in s:
        map1.append(s.index(characterS))
    print(map1)
    for characterT in t:
        map2.append(t.index(characterT))
    print(map2)
    if map1 == map2:
        return True
    return False

print(isIsomorphic("title", "paper"))