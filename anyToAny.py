def any_to_dec(system,number):
    result=0
    factor=len(number)
    for i in number:
        result+=(code_list.index(i)*system**(factor-1))
        factor-=1
    print("Na dziesietny to: ",result)
    return result
        
        
def dec_to_any(system,number):
    result=[]
    number=int(number)
    str_result=""
    while number!=0:
        modulo=number%system
        result.append(code_list[modulo])
        number=number//system
    for i in range(0,len(result)):
        str_result+=result[len(result)-1-i]
    print("A na ",system,"to: ",str_result)

    
code_list = ['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F","G","H","I",'J','K','L','M','N','O','P','Q','R','S','T','U','W','V',"X","Y","Z"]
current_system=int(input("Daj mnie system liczbowy"))
any_number=input("Gejw mi de namber")
dest_system=int(input("To tera daj mnie system do jakiego mam przekonwertowac"))


dec_to_any(dest_system,any_to_dec(current_system,any_number))
    