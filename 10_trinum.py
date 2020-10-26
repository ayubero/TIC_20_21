# -*- coding: cp1252 -*-
'''Realizar un programa que al recibir un número
entero muestre por pantalla los 3 números anteriores y
los 3 números siguientes al número recibido.'''
def trinumerador():
    num = int(input("Introduce un número entero: "))
    for i in range(-3, 4):
        print num + i

trinumerador()
