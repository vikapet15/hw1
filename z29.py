from math import*
a = int(input())
b = int(input())
c = int(input())
if (a > b+c or b > a+c or c > a+b) == 0:
    u1 = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
    u2 = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
    u3 = degrees(acos((a**2 + b**2 - c**2) / (2 * b * a)))
print(u1, u2, u3)