"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada
posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:
"""

from itertools import permutations

def eh_magico(v):
    soma = v[0] + v[1] + v[2]
    
    if v[3] + v[4] + v[5] != soma: return False
    if v[6] + v[7] + v[8] != soma: return False
    
    if v[0] + v[3] + v[6] != soma: return False
    if v[1] + v[4] + v[7] != soma: return False
    if v[2] + v[5] + v[8] != soma: return False
    
    if v[0] + v[4] + v[8] != soma: return False
    if v[2] + v[4] + v[6] != soma: return False
    
    return True

def mostrar(v):
    print(f"{v[0]} {v[1]} {v[2]}")
    print(f"{v[3]} {v[4]} {v[5]}")
    print(f"{v[6]} {v[7]} {v[8]}")
    print()

def quadrados_magicos():
    contador = 0
    for combinacao in permutations(range(1, 10)):
        if eh_magico(combinacao):
            mostrar(combinacao)
            contador += 1
    print(f"Total: {contador} quadrados mágicos")

quadrados_magicos()