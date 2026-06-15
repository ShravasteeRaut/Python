def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

n = int(input("Enter a number: "))
print("Sum =", sum_natural(n))