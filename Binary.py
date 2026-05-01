num = int(input("Enter a decimal number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = binary + str(rem)
    num = num // 2


binary = binary[::-1]

print("Binary equivalent:", binary)