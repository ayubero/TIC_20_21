# -*- coding: cp1252 -*-
import random

def adivinar():
    numero = random.randint(1,10)
    intentos = 0
    while True:
        intentos += 1
        intento = input("Adivina el n�mero, est� entre el 1 al 10, ambos incluidos: ")
        if intento == numero:
            print "Enhorabuena. Has adivinado el n�mero en el intento n�mero "+str(intentos)
            break
        elif intento < numero:
            print "El n�mero que has de adivinar es m�s grande"
        elif intento > numero:
            print "El n�mero que has de adivinar es m�s peque�o"
        else:
            "Error"

adivinar()
