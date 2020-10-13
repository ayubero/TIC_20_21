# Temporada equivale a la palabra año en este programa

def fechador(dia, mes, temporada):
    lista_meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]
    return str(dia)+" de "+lista_meses[mes-1]+" de "+str(temporada)
    
print(fechador(3,12,2009))
