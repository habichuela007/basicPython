def run ():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    #print(mi_diccionario)
    #print(mi_diccionario['llave1'])
    poblacion_paises = {
        'Argentina': 45646,
        'Brasil': 789798,
        'Colombia': 123132,
    }
    # for pais in poblacion_paises.keys():
    #     print(pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais,poblacion in poblacion_paises.items():
        print(pais+' tiene',str(poblacion)+' habitantes')

if __name__=='__main__':
    run()