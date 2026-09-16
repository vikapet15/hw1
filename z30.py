A = int(input('ATT: '))
C = int(input('COMP: '))
Y = int(input('YDS: '))
T = int(input('TD: '))
I = int(input('INT: '))
a = (C / A - 0.3) * 5
b = (Y / A - 3) * 0.25
c = (T / A) * 20
d = 2.375 - (I / A) * 25
a = max(0, min(a, 2.375))
b = max(0, min(b, 2.375))
c = max(0, min(c, 2.375))
d = max(0, min(d, 2.375))
rating = ((a + b + c + d) / 6) * 100
print(rating)