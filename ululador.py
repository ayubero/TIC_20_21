# -*- coding: cp1252 -*-
'''Haz un programa que lea la cadena y sustituya
las vocales por la letra u. Palabra de 10, ciclo for'''
def ululador(cadena):
    nueva_cadena = ""
    for item in cadena:
        if item == "a" or item == "e" or item == "i" or item == "o":
            nueva_cadena = nueva_cadena + "u"
        else:
            nueva_cadena = nueva_cadena + item
    return nueva_cadena

print ululador("Holaa,que?")
