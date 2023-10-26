def nestedListWeighSum(lst):
    depth = 0
    dict = {}
    for element in lst:
        while element[0]:
            depth += 1
            dict[element] = depth
            element = element[0]
    print(dict) 

print(nestedListWeighSum([[1,1],2,[1,1]]))
