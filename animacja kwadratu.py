def line_menager(width,height,distance):
    middle_x=width//2 +1
    middle_y=height//2 +1
    for i in range(1,height+1):
        for k in range(1,width+1):
            current_distance=max(abs(k-middle_x),abs(i-middle_y))
            if current_distance==distance:
                print("X", end="")
            else:
                print("-",end="")
        print("")
        
def frame_menager(maximal):
    for i in range(0,maximal):
        line_menager(width,height,i)
    for i in range(maximal-2,-1,-1):
        line_menager(width,height,i)
        
width=int(input("Podaj szerokość (nieparzystą!)"))
height=int(input("Podaj wyskość (nieparzystą!)"))
frame_menager((min(width,height)//2)+1)



