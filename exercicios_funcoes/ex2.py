"""
Criar um programa que calcula a partir de uma função o fatorial
de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Obs.:
Por propriedade, 0! = 1.
"""
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Insira o número para calcular a fatorial: "))
fatorial = fatorial(n)
print(f"O fatorial de {n} é {fatorial}")