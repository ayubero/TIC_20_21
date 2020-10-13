'''La función operar recibe dos números enteros,
los cuales son operados en función del valor de la variable operacion
S de suma
R de resta
M de multiplicación
D de división'''

def operar(num1, num2, operacion):
    operaciones = {
        "S": "+",
        "R": "-",
        "M": "*",
        "D": "/",
    }
    return eval(str(num1)+operaciones[operacion]+str(num2))

print(operar(5,3,"D"))
