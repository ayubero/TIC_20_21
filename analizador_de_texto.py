# -*- coding: cp1252 -*-
def analizar_texto(texto):
    vocales = ["a","e","i","o","u"]
    consonantes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    num_vocales = 0
    num_consonantes = 0

    for item in texto:
        for v in vocales:
            if item == v:
                num_vocales += 1
        for c in consonantes:
            if item == c:
                num_consonantes += 1
    return "Hay "+str(num_vocales)+" vocales y "+str(num_consonantes)+" consonantes"
            

#No introducir mayúsculas, tildes o ñ
print(analizar_texto("esto es una prueba"))
