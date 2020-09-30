# -*- coding: cp1252 -*-
def dia_de_la_semana(num):
    if num >= 1 and num <= 7:
        dias = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
        return dias[num - 1]
    else:
        return "no_valido"

dia_semana = dia_de_la_semana(input("Introduce un número entre 1 y 7: "))
if dia_semana  == "no_valido":
    print "No has introducido un valor válido"
else:
    print "Es " + dia_semana
