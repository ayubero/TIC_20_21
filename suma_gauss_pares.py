def suma_gauss_pares(num):
    suma_acumulada = 0
    for i in range(1, num+1):
        resto = i%2
        if resto == 0:
            suma_acumulada = suma_acumulada + i
    return suma_acumulada
            
print suma_gauss_pares(100)
