while True:
    a = input("Please enter a number: ")
    try:
        a = int(a)
    except ValueError:
        print("Please enter a valid number")
        continue
    if a == 0:
        break
    for i in range(2,a):
        if a % i == 0:
            print(f"{a} is not a prime number")
            break
    else:
        print(f"{a} is a prime number")