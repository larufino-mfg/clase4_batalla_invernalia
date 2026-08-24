import os
os.system("cls")

VIDIRIAGON_POR_SOLDADO = 3
TEMPERATURA_CONGELACION = -15
#################################################################################################################
cantidad_de_soldados_inmaculados = int(input("ingrese la cantidad de soldados inmaculados:"))

cantidad_de_soldados_dothrakis = int(input("ingrese la cantidad de soldados dothrakis:"))

cantidad_total_de_dagas = int(input("ingrese la cantidad de dagas de vidriagón disponibles en el castillo:"))

Temperatura_actual = float(input("ingrese la temperatura actual en invernalia:"))

daenerys_trajo_a_sus_dragones = input("¿Daenerys trajo a sus dragones? (si/no): ").lower()
########################################################################################
ejercito_total  = cantidad_de_soldados_inmaculados + cantidad_de_soldados_dothrakis

vidriagon = ejercito_total * VIDIRIAGON_POR_SOLDADO

deficit_de_armas = vidriagon - cantidad_total_de_dagas
######################################################################################

if ejercito_total >= 20000 and daenerys_trajo_a_sus_dragones == "si" and cantidad_total_de_dagas >= vidriagon:
    mensaje = "¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas."
elif ejercito_total >= 10000 and daenerys_trajo_a_sus_dragones == "si" and Temperatura_actual <= TEMPERATURA_CONGELACION or deficit_de_armas <= 0:
    mensaje = "Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_de_armas} dagas."
elif ejercito_total < 10000 and daenerys_trajo_a_sus_dragones == "si" and Temperatura_actual > TEMPERATURA_CONGELACION:
    mensaje = "Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur"
else:
    mensaje = "Derrota Total: El Rey de la Noche nos ha vencido. No hay esperanza para Invernalia."

































