# -*- coding: cp1252 -*-
import random

def adivinar():
    numero = random.randint(1,10)
    intentos = 0
    while True:
        intentos += 1
        intento = input("Adivina el número, está entre el 1 al 10, ambos incluidos: ")
        if intento == numero:
            print "Enhorabuena. Has adivinado el número en el intento número "+str(intentos)
            break
        elif intento < numero:
            print "El número que has de adivinar es más grande"
        elif intento > numero:
            print "El número que has de adivinar es más pequeño"
        else:
            "Error"

adivinar()
