"""
Criar um programa que calcula a partir de uma função o fatorial
de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Obs.:
Por propriedade, 0! = 1. Sem usar função recursiva
"""
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

while True:
    try:
        n = int(input("Insira o número para calcular a fatorial: "))
        break
    except ValueError:
        print("Por favor, insira um número válido.")

fatorial = fatorial(n)
print(f"A fatorial de {n} é {fatorial}")