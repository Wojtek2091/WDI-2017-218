import random
random.seed()
losowa=random.randrange(10)
trafil=False
while trafil==False:
    typ=int(input("wpisz liczbe"))
    if typ==losowa:
        print("Gratulacje trafiles!!!!!!")
        trafil=True
    elif typ<losowa:
        print("Podana liczba jest za mala, sprobuj jescze raz")
    elif typ>losowa:
        print("Podana liczba jest za duza, sprobuj jescze raz")