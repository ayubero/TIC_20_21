# -*- coding: cp1252 -*-
'''Realizar un programa que al recibir un n�mero
entero muestre por pantalla los 3 n�meros anteriores y
los 3 n�meros siguientes al n�mero recibido.'''
def trinumerador():
    num = int(input("Introduce un n�mero entero: "))
    for i in range(-3, 4):
        print num + i

trinumerador()
