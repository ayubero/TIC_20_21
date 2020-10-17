def calcular_salario(horas):
    salario = 0
    if (horas <= 40):
        salario = horas * 30
    else:
        primeras_cuarenta_horas = 40 * 30
        horas_extra = (horas - 40) * 45
        salario = primeras_cuarenta_horas + horas_extra
        
    return "Salario de:" + str(salario) + " €"

print(calcular_salario(50))
