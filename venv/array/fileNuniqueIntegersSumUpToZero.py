def sumZero(n: int):
    # generate some numbers from 1 -> n - 1
    # calculate the sum of these numbers, and then
    # multiply the sum of this with -1
    # resultArray = []
    # num = -1
    # sum = 0
    # if n == 2:
    #     resultArray.append(-1)
    #     resultArray.append(1)
    # else:
    #     for i in range(1, n):
    #         resultArray.append(num + i)
    #         sum += num + i
    #     resultArray.append(sum * -1)
    # return resultArray

    # solution 2 with better runtime complexity
    result = []
    if n % 2 != 0:
        result.append(0)
    for i in range(1, n, 2):
        result.append(i)
        result.append(-i)
    return result

print(sumZero(5))

