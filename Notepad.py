identical(a, b):
    if (a == b):
        return True
    else:
        return False

anyOdds(list1):
    for i in list1:
        if i%2 != 0:
            return True
    return False

oddSum(list1):
    sum = 0
    for i in list1:
        if i%2 != 0:
            sum += i
    return sum
