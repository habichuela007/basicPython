import random


def generate_password():
    capital = ['A','B','C','D','E','F','G']
    lower = ['a','b','c','d','e','f','g']
    symbol_password = ['!','@','#','$','%','ˆ','&']
    number_pass = ['1','2','3']

    characters_passwd = capital + lower + symbol_password + number_pass

    password = []

    for i in range(15):
        random_character = random.choice(characters_passwd)
        password.append(random_character)
    password = ''.join(password)
    return password




def run():
    password = generate_password()
    print('Your suggested password is: ' + password)

if __name__=='__main__':
    run()