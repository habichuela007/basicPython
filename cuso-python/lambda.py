from functools import reduce

def run():
    #my_list = [1,4,5,6,9,13,19,21]
    # odd = [i for i in my_list if i % 2 !=0]
    
    #odd = list(filter(lambda x: x%2 !=0, my_list))
    #print(odd)

    # #Comprehensions
    # my_list = [1,2,3,4,5]
    # # squares = [i**2 for i in my_list]

    # #aplicando map
    # squares = list(map(lambda x: x**2, my_list))
    # print(squares)

    # my_list = [2,2,2,2,2]
    # all_multiplied = 1
    # for i in my_list:
    #     all_multiplied = all_multiplied*i
    # print(all_multiplied)

    #REDUCE, lambda lleva dos parámetros, en la primera iteración va a ser el primer elemento de nuestra lista y el segundo elemento de nuestra lista, el resultado de eso se multiplica con el tercero, etc.
    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print(all_multiplied)




if __name__=='__main__':
    run()
