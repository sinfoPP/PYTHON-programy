#napis="kotek"
"""
napis=2
napis=input()
print("tekst",napis)
"""
#napis=input()
#print (napis,"lat")



"""
import random
random.seed()
szukana=random.randint(10,20)
licznik=0
while 1:
    czytana=int(input())
    licznik+=1
    if czytana < szukana:
        print("za mała")
    elif czytana > szukana:
        print("za duze") 
    else: 
        print("zgadłeś za",licznik,"podejsciem")
        break
#koniec


"""
"""
import random

random.seed()

while 1:
    print("podaj liczbe początkową")
    poczatek=int(input())
    print("podaj liczbe koncową")
    koniec=int(input())
    if koniec<poczatek:
        print("wpisz liczbe poczatkową mniejszą od koncowej jeszcze raz")
    else:
        break
        
szukana=random.randint(poczatek,koniec)        
licznik=0
while 1:
    czytana=int(input())
    licznik+=1
    if czytana < szukana:
        print("za mała")
    elif czytana > szukana:
        print("za duze") 
    else: 
        print("zgadłeś za",licznik,"podejsciem")
        break


"""

#silnia
#tu bedzie funkcja
def silnia(arg1):
    if arg1 > 1:
       return (arg1 * silnia (arg1-1))
    else :
        return 1
    
    

#
#reszta
wartosc=""
while not wartosc.isdigit():
     wartosc=input("podaj wartosc")
     #if wartosc.isdigit():

print(silnia(int(wartosc)))

"""
"""

     

        




 






