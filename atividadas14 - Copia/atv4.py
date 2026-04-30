"""
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
"""
for i in range (5):
    numero = int(input("Insira um número: "))
    if i == 0:
        n1 = numero
    if i == 1:
        n2 = numero
    if i == 2:
        n3 = numero
    if i == 3:
        n4 = numero
    if i == 4:
        n5 = numero
for i in range(4):
    if n1 > n2:
        caixa = n1
        n1 = n2
        n2 = caixa
    if n2 > n3:
        caixa = n2
        n2 = n3
        n3 = caixa
    if n3 > n4:
        caixa = n3
        n3 = n4
        n4 = caixa
    if n4 > n5:
        caixa = n4
        n4 = n5
        n5 = caixa
print(n1, n2, n3, n4, n5)