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
    for i in range(0,101,2):
        wynik - wynik + 1
            
    print(wynik)
    
def sumuj_wprowadzone():
    
    ile = int(input('ile podasz liczb? '))
    wynik = 0
    for z in range(ile):
        liczba = int(input('Podaj liczbe: '))
        wynik = wynik + liczba
        
    print(wynik)



    




def main(args):
    # [0, 1, 2, 3, 4]
    # suma_parzystych()
    # suma_nieparzystych()
    sumuj_wprowadzone()
 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
