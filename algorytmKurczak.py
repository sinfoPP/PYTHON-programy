czas=0
kurczak_jest=0
rodzaj_programu=0
kurczak_piec=0
#komunikaty - start
kom_0="koniec.brak kurczaka"
kom_1="kurczak taki sobie"
kom_2="kurczak bajer"
rodzaj_1 = "1-krótki program.kurczak krwisty\n"
rodzaj_2 = "2-krótki program.kurczak miałki\n"
rodzaj_3 = "3-krótki program.kurczak sucharek\n"
kom_r_1="czas programu 20-30min"
kom_r_2="czas programu 40-50min"
kom_r_3="czas programu 60-70min"
kom_r_b_1="czas za krótki"
kom_r_b_2="czas za dlugi"
#komunikaty -  koniec

#pobranie informacji
kurczak_jest=int(input("czy masz kurczaka ?"))
if kurczak_jest == 0:
    print(kom_0)
    exit
elif kurczak_jest == 1:
    
    print("wybierz rodzaj programu\n",rodzaj_1,rodzaj_2,rodzaj_3)
    rodzaj_programu=int(input("podaj rodzaj programu: "))
    if rodzaj_programu == 1:
        print (kom_r_1)
        czas=int(input("czas: "))#procedura sprawdzajaca
        if 20 <= czas <= 30:
            print(kom_1)
            
        elif czas < 20:
            print(kom_r_b_1)
        elif czas > 30:
            print(kom_r_b_2,"\n",kom_1)
                
                
        elif kurczak_piec == 2:
            print (kom_r_2)
            czas=int(input("czas: "))
        elif kurczak_piec == 3:
            print (kom_r_3)
            czas=int(input("czas: "))
        
        

#wyjscie 1
#print(kom_1)
#exit
#wyjscie 2
print(kom_2)
