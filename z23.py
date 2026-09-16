a = int(input())
ch = a // 3600
m = (a % 3600) // 60
s = a % 3600 % 60
print(f"{ch} часов {m} минут {s} секунд")