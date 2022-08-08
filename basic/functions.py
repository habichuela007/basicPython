# def printMessage(): # def::palabra clave para declara funciones
#     print('Mensaje especial')
#     print('Estoy aprendiendo a usar funciones')

# printMessage()
# printMessage()
# printMessage()

def conversation(mensaje):
    print('Hola')
    print('Como estás')
    print(mensaje)
    print('Adios')

option = int(input('Choose an option (1,2,3): '))
if option == 1:
    conversation('Elegiste la opcion 1')
elif option == 2:
    conversation('Elegiste la opcion 2')
elif option == 3:
    conversation('Elegiste la opcion 3')
else:
    print('write a valid number')


def suma(a,b):
    print('Se suman dos números')
    result = a+b
    return result #para regresar el valor del resultado de la varialbe en la funcion
    
