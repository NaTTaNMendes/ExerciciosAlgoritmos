from math import sqrt

i1 = float(input("Informe o primeiro lado: "))
i2 = float(input("Informe o segundo lado: "))
i3 = float(input("Informe o terceiro lado: "))

i = (i1 + i2 + i3) / 2
area = sqrt(i * (i - i1) * (i - i2) * (i - i3))

print("Área:",area)
