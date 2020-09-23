# Dibujar un cuadrado ASCII

# Obtener las dimensiones
n_col = int(input("Número de columnas:"))
n_fil = int(input("Número de filas:"))

for fila in range(0, n_fil):
    for columna in range(0, n_col):
        if fila == 0: # Dibujar primera fila
            if columna == 0:
                print("╔", end="")
            elif columna == n_col-1:
                print("╗", end="")
            else:
                print("═", end="")
        elif fila == n_fil-1: # Dibujar la última fila
            if columna == 0:
                print("╚", end="")
            elif columna == n_col-1:
                print("╝", end="")
            else:
                print("═", end="")
        else: # Dibujar el resto de filas
            if columna == 0:
                print("║", end="")
            elif columna == n_col-1:
                print("║", end="")
            else:
                print(" ", end="")
    print(" ")
