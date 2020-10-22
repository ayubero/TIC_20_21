# -*- coding: cp1252 -*-
def multiplicar():
    multiplicacion = 1
    for i in range(4):
        num = input("Introduce el número "+str(i+1)+":")
        if type(num) == int:
            multiplicacion = multiplicacion*num
        else:
            print "No has introducido un número"
    print "Producto: " + str(multiplicacion)
        
multiplicar()
