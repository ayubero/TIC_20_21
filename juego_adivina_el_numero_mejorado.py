# -*- coding: cp1252 -*-
import random

def adivinar():
    #Obtener intervalo
    comienzo = 0
    final = 0
    intervalo = str(input("Introduce un intervalo de números enteros en formato matemático para comenzar a jugar. Ej. (0,3]: "))
    intervalo_array = intervalo.split(",")
    comienzo_string = intervalo_array[0]
    if comienzo_string[0:1] == "(":
        comienzo = int(comienzo_string[1:]) + 1
    elif comienzo_string[0:1] == "[":
        comienzo = int(comienzo_string[1:])
    else:
        print("Introduce un intervalo válido")
        adivinar()
        return
    final_string = intervalo_array[1]
    if final_string[-1] == ")":
        final = int(final_string[:-1]) - 1
    elif final_string[-1] == "]":
        final = int(final_string[:-1])
    else:
        print("Introduce un intervalo válido")
        adivinar()
        return

    if comienzo > final:
        print("El número de comienzo del intervalo no puede ser superior al final")
        adivinar()
        return

    #Jugar
    numero = random.randint(comienzo,final)
    intentos = 0
    while True:
        intentos += 1
        intento = int(input("Adivina el número, está entre el "+str(comienzo)+" al "+str(final)+", ambos incluidos: "))
        if intento == numero:
            print("Enhorabuena. Has adivinado el número en el intento número "+str(intentos))
            break
        elif intento < numero:
            print("El número que has de adivinar es más grande")
        elif intento > numero:
            print("El número que has de adivinar es más pequeño")
        else:
            "Error"

adivinar()
