def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1,2,3))
print(sum(8,9,10,11,12,13))
print(sum())

sum_2 = lambda a,b: a+b

print(sum_2(1,2))