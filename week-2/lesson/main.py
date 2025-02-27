# loops
# Used in order to repeat an action for a definite or
# indefinite amount

for i in range(5):
    print(i)
print("For loop ended")

for i in range(8,10):
    print(i)

for i in range(5,50,5):
    print(i)

students = ["Ali","Aybüke","Büşra","Deniz"]

for student in students:
    if student == "Büşra":
        break
    print(f"Making calculation: {student}")

x = 50
while x < 100:
    print(x)
    x += 1

user_input = input("Enter a value, or press q to exit: ")

while user_input != "q":
    print(f"Value: {user_input}")

