import json
from difflib import get_close_matches

data = json.load(open("data.json")) #Biblioteca de um dicionário em inglês

def dicionario(palavra):

    palavra = palavra.lower()       #Certifica que o que for inserido será transformado em somente minúsculas
    if palavra in data:             #Certifica que a palavra está no dicionário
        return data[palavra]

    elif palavra.title() in data:
        return data[palavra.title()]

    elif palavra.upper() in data:
        return data[palavra.upper()]

    elif len(get_close_matches(palavra , data.keys())) > 0:
        yn = input( "Did you mean %s instead? (Y - Yes // N - No) " % get_close_matches(palavra , data.keys())[0] )
        
        if   yn == "Y":
            return data[get_close_matches(palavra, data.keys())[0]]
        
        elif yn == "N":
            return "We didn't understand your entry."

    else:
        return "The word doesnt exist. Please double check it" 
    

palavra = input("Insira a palavra em inglês: ")

output = dicionario(palavra)

if type(output) == list :
    for item in output:
        print(item)
else:
    print(output)