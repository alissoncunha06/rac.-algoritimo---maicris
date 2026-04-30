"""
Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.
"""
nome = input("Insira o seu nome completo: ")
primeiro = ""
ultimo = ""
for letra in nome:
    if letra != " ":
        primeiro += letra
    else:
        break
for i in range(len(nome) - 1, -1, -1):
    if nome[i] != " ":
        ultimo = nome[i] + ultimo
    else:
        break
print(primeiro, ultimo)