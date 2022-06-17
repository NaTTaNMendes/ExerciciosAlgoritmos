def conversorBinario(q):
    resultado = ""
    while q != 0:
        r = q % 2
        resultado = str(r) + resultado
        q = q // 2
    return resultado

q = 25
print("Valor em decimal: %.0f \nValor em binário: %s" % (q, conversorBinario(q)))