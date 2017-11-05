# Pół choinka pozdrawin W.S
rozmiar=int(input("dej mnie rozmiar choinki"))
if rozmiar<2:
    print("za maly!!")
else:
    liczba_trojkatow=rozmiar
    for k in range(1,liczba_trojkatow):
        liczba_poziomow=k+1
        for i in range(0,liczba_poziomow):
            liczba_znakow=i+1
            for j in range(0,liczba_znakow):
                print("x" ,end="")
            print() 