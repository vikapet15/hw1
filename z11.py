from math import*
r1 = float(input())
r2 = float(input())
R = max(r1, r2)
r = min(r1, r2)
S = pi * R**2 - pi * r**2
print(S)
