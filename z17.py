w = float(input('вес: ')) * 0.453592
h = float(input('высота: ')) * 0.0254
IMT = w / h**2
print(round(IMT, 2))