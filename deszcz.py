import random
import time
import os

def printline(n,width):
    if n<=width:
        for i in range(0,n-1):
            print("0", end="")
        print("X", end="")
        for i in range(n,width):
            print("0", end="")
        print("")
    else:
        for i in range(0,width):
            print("0",end="")
        print("")
    
def linemenager(x_pos,width):
    for i in range(0,int(len(x_pos))):
        printline(x_pos[i],width)
    
    
     
random.seed()
position_list=[]
width=int(input("podaj szerokość"))
height=int(input("podaj wysokość"))
for i in range(0,height):
    position_list.append(width+2)
linemenager(position_list,width)
time.sleep(0.3)
for i in range(0,10):
    column=random.randrange(width)
    position_list.insert(0,column)
    del position_list[len(position_list)-1]
    linemenager(position_list,width)
    print("")
    time.sleep(0.3)

printline(1,5)
printline(1,6)
