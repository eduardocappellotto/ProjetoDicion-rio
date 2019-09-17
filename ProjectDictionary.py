import json
from difflib import get_close_matches

data = json.load(open("data.json")) #Biblioteca de um dicionário em inglês

def dicionario(palavra):

    palavra = palavra.lower()       #Certifica que o que for inserido será transformado em somente minúsculas
    if palavra in data:             #Certifica que a palavra está no dicionário
        return data[palavra]

    elif len(get_close_matches(palavra , data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(palavra , data.keys())[0]
        

    else: return "A palavra não existe, verifique a inserção"

palavra = input("Insira a palavra em inglês: ")

print( dicionario(palavra))
