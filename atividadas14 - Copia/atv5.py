"""
Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B.
"""
a = 5000000
b = 7000000
tempoi = 0
while a <= b:
    a += a*0.03
    b += b*0.02
    tempoi += 1
print("demora", tempoi, "anos para a população a alcançar a b")