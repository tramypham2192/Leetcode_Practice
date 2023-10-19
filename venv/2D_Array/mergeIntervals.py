def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []

    for element in intervals:
        if len(result) == 0 or result[-1][1] < element[0]:
            result.append(element)
        else:
            result[-1][1] = max(result[-1][1], element[1])
    return result

# print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[2,3]]))





