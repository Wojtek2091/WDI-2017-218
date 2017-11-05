## cała choinka xD pozdrawin W.S
rozmiar=int(input("podaj rozmiarr"))
if rozmiar<1:
    print("za maly!!!")
else:
    for i in range(0,rozmiar):
        liczba_poziomow=i+2
        for k in range(0,liczba_poziomow):
            liczba_spacji=rozmiar-k
            liczba_znakow=2*k
            for j in range(0,liczba_spacji):
                print(" ",end="")
            for l in range(0,liczba_znakow+1):
                print("x",end="")
        
            print()