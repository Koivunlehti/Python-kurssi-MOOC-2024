from math import sqrt

a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

root_1 = (-b + sqrt(b**2-4*a*c))/(2*a)
root_2 = (-b - sqrt(b**2-4*a*c))/(2*a)

print(f"Juuret ovat {root_1} ja {root_2}")