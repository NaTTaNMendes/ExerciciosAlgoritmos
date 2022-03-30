import math

t1 = float(input("INFORME A PRIMEIRA LATITUDE EM GRAUS:"))
g1 = float(input("INFORME A PRIMEIRA LONGITUDE EM GRAUS:"))
t2 = float(input("INFORME A SEGUNDA LATITUDE EM GRAUS:"))
g2 = float(input("INFORME A SEGUNDA LONGITUDE EM GRAUS:"))

t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

distancia = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print("Distância em KM: %.2f" % distancia)
