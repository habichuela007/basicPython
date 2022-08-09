from queue import PriorityQueue


def conversor(typePeso,dollarValue):
    pesos = input("How many " + typePeso+ " Pesos do you have? ")
    pesos = float(pesos)
    dollars = pesos/dollarValue
    dollars = round(dollars,2)
    dollars = str(dollars)
    print("TIenes $"+ dollars + "dolares")
    

menu = """
Welcome to the exchange conversor

1 - Colombian Peso
2 - Argentinian Peso
3 - Mexican Peso

Choose an option

"""
option = int(input(menu))
#print(menu)
if option ==1:
    conversor("Colombian",3875)
elif option ==2:
    conversor("Argentinian",65)
elif option ==3:
    conversor("Mexican",65)
else:
    print("Ingrese una opción válida")