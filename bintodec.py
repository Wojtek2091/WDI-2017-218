def z2na10(bin_var):
    factor=len(bin_var)-1
    wynik=0
    for i in bin_var:
        wynik+=int(i)*2**factor
        factor-=1
    print(wynik)
        
        
        
bin=input("podaj liczbe binarna")
liczymy=True
for i in bin:
    if (int(i)!=1) & (int(i)!=0):
        print("bledna liczba binarna!")
        liczymy=False
        
        
if liczymy==True:
    z2na10(bin)