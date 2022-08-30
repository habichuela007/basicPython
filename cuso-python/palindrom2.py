import string


def palindrom ():
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string == stringp[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrom(""))
except TypeError:
    print("Solo se pueden ingresar enteros")

def run ():
    print('Hola')

if __name__=='__main__':
    run()