# Quadratic equation solver
import math

a = int(input("Enter coefficient of a :"))
b = int(input("Enter coefficient of b :"))
c = int(input("Enter coefficient of c :"))
d = b ** 2 - 4 * a * c
if d < 0:
    print("no solution")

elif d == 0:
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a

else:
    x1 = (-b - math.sqrt((b**2)-(4*a*c)))/ (2 * a)
    x2 = (-b + math.sqrt((b**2)-(4*a*c)))/( 2 * a)
    print("solutions are", x1, "and", x2)