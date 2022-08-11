def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue #no se imprime lo que está debajo del continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 4521:
    #         break

    texto = input('Escibre un texto: ')
    for letra in texto: # recorrer cadena de caracteres
        if letra == 'o':
            break
        print(letra)


if __name__=='__main__':
    run()