def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return(True)
    else:
        return(False) 
#siempre hay que dejar DOS espacios entre funciones


def run(): #Siempre hay que poner una función principal, 
    palabra = input('Escribe una palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print(palabra+' Es palindromo')
    else:
        print(palabra+' NO es palindromo')


if __name__ == '__main__': #es el entry point
    run()