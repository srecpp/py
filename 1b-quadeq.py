import math
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = b * b - 4 * a * c
root1 = (-b + math.sqrt(abs(d))) / (2.0 * a)
root2 = (-b - math.sqrt(abs(d))) / (2.0 * a)
print("Root 1 = ", root1)
print("Root 2 = ", root2)
