def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    hset = set()
    while n != 1:
        if n in hset:
            return False
        hset.add(n)
        # n = sum([int(i) ** 2 for i in str(n)])
        sum = 0
        for i in str(n):
            sum += int(i) ** 2
            n = sum
    return True

print(isHappy(19))

