import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

length = int(input("Enter the password length: "))

if length < 3:
    print("Password length should be at least 3.")
else:
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]

    all_characters = lowercase + uppercase + numbers

    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    password = "".join(password)

    print("Generated Password:", password)
