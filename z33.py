N = int(input())
C = int(input())
Z = int(input())
P = (Z - 1) // (N * C) + 1
P2 = (Z - 1) % (N * C)
STB = P2 // N + 1
STR = P2 % N + 1
print(f"страница {P} столбец {STB} строка {STR}")
