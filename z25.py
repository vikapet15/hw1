X,Y,N = map(int,input().split())
k = (Y * N) % 100
r = X * N + (Y * N) // 100
print(f"{r} руб. {k} коп.")