import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Ingresa un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas PEQUEÑO')
        numero_elegido = int(input('Ingresa un número del 1 al 100: '))                       
    print('GANASTE')

if __name__=='__main__':
    run()