def calculate_tax(price, rate=0.2):
    return price + price * rate

print(calculate_tax(100,0.5))
print(calculate_tax(30))

def sum(*a):
    result = 0
    for n in a:
        result += n
    return result

print(sum(1,5,6,7,8,9))

add = lambda a,b: a+b
print(add(10,20))