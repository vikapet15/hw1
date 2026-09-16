X,Y = map(int, input().split())
res = 1 // ((X % Y) * (Y % X) + 1)
print(res)
