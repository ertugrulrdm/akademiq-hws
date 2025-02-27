def calculator(n1, n2, type):
    if type == '+':
        return n1 + n2
    elif type == '-':
        return n1 - n2
    elif type == '*':
        return n1 * n2
    elif type == '/':
        return n1 / n2

while True:
    type = input("Please enter the type of operation:")
    if type not in ['+', '-', '*', '/']:
        print("Invalid operation")
        continue
    try:
        n1 = int(input("Please enter the first number:"))
        n2 = int(input("Please enter the second number:"))
    except ValueError:
        print("Please enter valid numbers")
        continue
    if type == '/' and n2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"{n1} {type} {n2} = {calculator(n1, n2, type)}")

