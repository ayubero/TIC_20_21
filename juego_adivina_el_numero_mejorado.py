# -*- coding: cp1252 -*-
import random

def adivinar():
    #Obtener intervalo
    comienzo = 0
    final = 0
    intervalo = str(input("Introduce un intervalo de n�meros enteros en formato matem�tico para comenzar a jugar. Ej. (0,3]: "))
    intervalo_array = intervalo.split(",")
    comienzo_string = intervalo_array[0]
    if comienzo_string[0:1] == "(":
        comienzo = int(comienzo_string[1:]) + 1
    elif comienzo_string[0:1] == "[":
        comienzo = int(comienzo_string[1:])
    else:
        print("Introduce un intervalo v�lido")
        adivinar()
        return
    final_string = intervalo_array[1]
    if final_string[-1] == ")":
        final = int(final_string[:-1]) - 1
    elif final_string[-1] == "]":
        final = int(final_string[:-1])
    else:
        print("Introduce un intervalo v�lido")
        adivinar()
        return

    if comienzo > final:
        print("El n�mero de comienzo del intervalo no puede ser superior al final")
        adivinar()
        return

    #Jugar
    numero = random.randint(comienzo,final)
    intentos = 0
    while True:
        intentos += 1
        intento = int(input("Adivina el n�mero, est� entre el "+str(comienzo)+" al "+str(final)+", ambos incluidos: "))
        if intento == numero:
            print("Enhorabuena. Has adivinado el n�mero en el intento n�mero "+str(intentos))
            break
        elif intento < numero:
            print("El n�mero que has de adivinar es m�s grande")
        elif intento > numero:
            print("El n�mero que has de adivinar es m�s peque�o")
        else:
            "Error"

adivinar()
