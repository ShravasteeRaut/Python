try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age entered.")

    if age % 2 == 0:
        print("Age is Even.")
    else:
        print("Age is Odd.")

except ValueError as ex:
    print("Invalid age:", ex)




