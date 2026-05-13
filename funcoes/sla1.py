"""
recursividade de funcoes
"""
#funcao recursiva para somar os antecessores de um numero
def somar_ant(n):
    if n == 1:
        return 1
    return n + somar_ant(n-1)

n = int(input("Digite o valor para somar os antecessores: "))
soma = somar_ant(n)
print(f"A soma dos antecessores de {n} é {soma}")