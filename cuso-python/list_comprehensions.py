def run():
    # squares = []
    # for i in range(1,101):
    #     squares.append(i**2)
    # print(squares)

    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # print(squares)
    
    # squares = [i**2 for i in range(1,101) if i % 3 !=0]

    # RETO

    squares = [i*4 for i in range(1,1000) if i % 36 !=0]
    print(squares)

if __name__=='__main__':
    run()