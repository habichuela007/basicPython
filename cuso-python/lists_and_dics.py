def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {'firstname':'Gabriel','lastname':'Santamaria'}

    super_list = [
        {'firstname':'Gabriel','lastname':'Santamaria'},
        {'firstname':'Muguel','lastname':'Arias'},
        {'firstname':'Susana','lastname':'Martinez'},
        {'firstname':'Juan','lastname':'Santamaria'}
    ]

    super_dic = {
        'natural_nums':[1,2,3,4,5],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums':[1.1,4.5,6.43],
    }

    for key, value in super_dic.items():
        print(key, '-', value)

    for i in super_list:
        print(i['firstname'],i['lastname'])

if __name__=='__main__':
    run()