import time


def silniarek(n):
    wynik=1
    if n==0:
        wynik=1
    if n==1:
        wynik=1
    else:
        wynik=n*silniarek(n-1)
    return wynik
        
def silniait(n):
    wynik=1
    if n==0:
        wynik=1
    if n==1:
        wynik=1
    else :
        for i in range(1,n+1):
            wynik*=i
    return wynik
    
zmienna=int(input("podaj liczbe"))
start_time=time.time()
print("Silnia rekurencyjnie: ",silniarek(zmienna),"--- %s seconds ---" % (time.time() - start_time))
start_time=time.time()
print("Silnia iteracyjnie: ",silniait(zmienna),"--- %s seconds ---" % (time.time() - start_time))
