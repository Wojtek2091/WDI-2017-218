rozmiar=int(input("podaj rozmiar choinki"))
z=rozmiar-1
for i in range(1,rozmiar):
    for j in range(1,z):
        print(" ", end=" ")
    for k in range(1,2):
         print("x",end="")