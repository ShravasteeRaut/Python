import math

x = float(input("Enter angle in degrees: "))
x = x * math.pi / 180   

sin = 0
cos = 0

for i in range(10):
    sin += ((-1)**i * x**(2*i+1)) / math.factorial(2*i+1)
    cos += ((-1)**i * x**(2*i)) / math.factorial(2*i)

tan = sin / cos

print("Sin =", sin)
print("Cos =", cos)
print("Tan =", tan)