# Dibujar un cuadrado hecho de cuadrados

# Obtener las dimensiones del cuadrado
n_col = int(input("Número de columnas:"))
n_fil = int(input("Número de filas:"))
estaPintado = True;

for fila in range (0, n_col):
    for columna in range(0, n_fil):
        # Pintar en cada "celda" un cuadrado lleno o vacío en función de la variable estaPintado
        if estaPintado:
            print("■ ", end="")
        else:
            print("□ ", end="")
        estaPintado = not estaPintado # Cambiar el valor de estaPintado por el opuesto
    print(" ")
