#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma_parzystych():
    wynik = 0
    for i in range(0,101,2):
        print(i)
        wynik = wynik + i

    print(wynik)
    
def suma_nieparzystych():
    wynik = 0
    for i in range(0,101,3):
        wynik - wynik + i
            
    print(wynik)
    
def sumuj_liczby():
    """
    funkcja pobiera ;iczby od uzytkownika i sumuje dopkuji suma nie przekroczy wartosci 75.
    """

    suma = 0
    while suma < 75:
        liczba = int(input('Podaj liczbe: '))
        suma = suma + liczba
        
    print("suma liczba:", suma)



    




def main(args):
    sumuj_liczby()
    # [0, 1, 2, 3, 4]
    # suma_parzystych()
    # suma_nieparzystych()

 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
