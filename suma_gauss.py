def suma_gauss(num):
    suma_acumulada = 0
    for i in range(1, num+1):
        suma_acumulada = suma_acumulada + i;
    return suma_acumulada

print suma_gauss(100)
