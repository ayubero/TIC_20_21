'''Escribe un programa que procese un conjunto de edades
y devuelva la edad del mayor, la edad del menor,
la edad media y la diferencia de edaes entre el mayor y el menor'''

def edad_media(edades):
    edades.sort() #Ordenar el array
    l_edades = len(edades) #Obtener la longitud del array
    edad_menor = 0
    edad_mayor = 0
    edad_acumulada = 0.0
    for i in range(l_edades):
        edad_acumulada = edad_acumulada + edades[i]
        if i == 0:
            edad_menor = edades[0]
        elif i == l_edades - 1:
            edad_mayor = edades[i]
    print "Edad menor: " + str(edad_menor)
    print "Edad mayor: " + str(edad_mayor)
    diferencia_edades = edad_mayor - edad_menor
    print "Diferencia de edades mayor y menor: " + str(diferencia_edades)
    print "Suma de todas las edades: " + str(edad_acumulada)
    edad_media = edad_acumulada / l_edades
    print "Edad media: " + str(edad_media)
    
array_edades = [13,12,15,19,23,17,7,24,6]
edad_media(array_edades)
