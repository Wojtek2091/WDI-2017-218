def element(l,e):
    if l==1 or l==2 or e==1 or e==l:
        return 1
    else:
        return element(l-1,e-1)+element(l-1,e)
 
def triangle(h):
    for l in range(1,h+1):
        print(" "*(h-l)*3,end=" ")
        for e in range(1,l+1): 
            print("{:^6}".format(str(element(l,e))),end="")
        print("")

h=int(input("wysokoć"))
triangle(h)
