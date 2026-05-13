"""
Criar um programa que receba uma lista de números e retorne a
média dos mesmos.
"""
def calcular_media(lista):
    if sum(lista) != 0:
        return sum(lista) / len(lista)
    else:
        print("Não é possível divisão por zero")
        return 0

lista = []

while True:
    try:
        num = float(input("Insira um número (ou 0 para sair): "))
        if num == 0:
            break
        lista.append(num)
    except ValueError:
        print("Por favor, insira um número válido.")

media = calcular_media(lista)
print(f"A média dos números inseridos é: {media:.2f}")