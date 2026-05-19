import random

def embaralhar(palavra):
    palavra = palavra.lower()
    letras = list(palavra)
    random.shuffle(letras)
    return "".join(letras)

texto = input("Digite umapalavra: ")
print(embaralhar(texto))