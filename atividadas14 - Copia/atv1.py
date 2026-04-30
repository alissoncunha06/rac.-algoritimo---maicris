"""
1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos.
"""
tempo = 0
gramas = float(input("Digite a massa inicial em gramas: "))
while gramas >= 0.5:
    gramas = gramas/2
    tempo += 50
minutos = tempo // 60
segundos = tempo % 60
print(f'demora {minutos} minutos e {segundos} segundos para que a massa chegue a {gramas}')