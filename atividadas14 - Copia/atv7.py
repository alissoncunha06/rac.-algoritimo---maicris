"""
Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras.
"""
contador = 0
while True:
    palavra = input("Insira uma palavra: ")
    if palavra == "":
        break
    for letra in palavra:
        if letra == "a" or letra == "A":
            contador += 1
print(contador)