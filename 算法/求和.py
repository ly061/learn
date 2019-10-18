def sum(num):
    sum1 = 0
    for i in range(len(str(num))):
        sum1 += int(str(num)[i])
    return sum1


print(sum(122))
