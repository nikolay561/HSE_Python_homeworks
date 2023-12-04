def sum_distance(x, y):
    result = []
    if x < y:
        for number in range(x, y+1):
            result.append(number)
    else:
        for number in range(y, x+1):
            result.append(number)
    return sum(result)


print(sum_distance(10, 20))
