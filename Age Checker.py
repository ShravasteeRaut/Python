age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 13:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")