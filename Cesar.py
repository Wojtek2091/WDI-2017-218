def textFormat(text):
    text.lower()
    formatedText=""
    for ch in text:
        if ch.isalpha():         
            formatedText+=ch
    return formatedText.lower()
    
def cesarCode(text,shift):
    text=textFormat(text)
    finalText=""
    finalLetter=''
    for ch in text:
        letterCode=ord(ch)
        newCode=letterCode+shift
        if newCode > ord("z"):
            newCode-=26
        elif newCode < ord('a'):
             newCode+=26
                
        finalLetter=chr(newCode)

            
        finalText+=finalLetter
    return finalText
    
def decode(text,shift):
    return cesarCode(text,-shift)
    
print (cesarCode('AGH to Super uczelnia',3))
print (decode("djk",3))
