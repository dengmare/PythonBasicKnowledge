def fuck(x):
    sum = 1
    for num in range(1,x+1):
        print num
        sum *= num
    return sum

print fuck(5)
