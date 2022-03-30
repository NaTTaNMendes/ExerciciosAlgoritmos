from math import pi
from math import tan

i = float(input("Informe o comprimento: "))
n = int(input("Informe o número de lados: "))

area = (n * (i ** 2)) / (4 * tan(pi/n))

print("Área:",area)
