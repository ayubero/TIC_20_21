# -*- coding: cp1252 -*-
def analizar_texto(texto):
    vocales = ["a","e","i","o","u"]
    num_vocales = 0

    for item in texto:
        for v in vocales:
            if item == v:
                num_vocales += 1
        for c in consonantes:
            

#No introducir may�sculas, tildes o �
analixar_texto("esto es una prueba")
