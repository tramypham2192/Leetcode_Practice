def hammingWeight(n):
    result = 0
    for i in range(len(str(bin(n)[2:]))):
        if str(bin(n)[2:])[i] == str(1):
            result += 1
    return result

print(hammingWeight(11))
