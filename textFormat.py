def textFormat(text):
    text.lower()
    formatedText=""
    for ch in text:
        if ch.isalpha():         
            formatedText+=ch
    return formatedText.lower()
    
print(textFormat("Si e7ma"))