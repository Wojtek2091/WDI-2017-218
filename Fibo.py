import time

def fiborek(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fiborek(n-1)+fiborek(n-2)

def fiboit(n):
    preprevious=0
    previous=1
    result=0
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2,n):
            result=preprevious+previous
            preprevious=previous
            previous=result
        return result
            
    
    
    
    
    
zmienna=int(input("podaj wyraz ktory mam obliczyc"))  
start_time=time.time()
print("fibonnaci rekurencyjnie: ",fiborek(zmienna),"--- %s seconds ---" % (time.time() - start_time))
start_time=time.time()
print("fibbonaci iteracyjnie: ",fiboit(zmienna),"--- %s seconds ---" % (time.time() - start_time))