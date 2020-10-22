# -*- coding: cp1252 -*-
def convertir_dol_a_eur():
    dolares = input("Introduce el número de dólares que quieres convertir a euros: ")
    if type(dolares) == int or type(dolares) == float:
        print str(dolares*0.85) + " €"
    else:
        print "No has introducido un número válido"

convertir_dol_a_eur()
