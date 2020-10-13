# Calculadora de IVA en función de su tipo (general, reducido, superreducido)
def calcular_iva(num, tipo):
   tipos_de_iva = {
       "general": 0.16,
       "reducido": 0.07,
       "superreducido": 0.04
    }

   iva = num * tipos_de_iva[tipo]
   return num + iva;

print(calcular_iva(100, "reducido"))
