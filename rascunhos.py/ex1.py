lista = list()

for i in range(5):
    while True:
        try:
            num = int(input('digite um valor int: '))
            lista.append(num)
            break
        except ValueError:
            print('valor invalido')

def maior(lista):
    maior = lista[0]
    for v in lista:
        if v > maior:
            maior = v
    return maior

def menor(lista):
    menor = lista[0]
    for z in lista:
        if z < menor:
            menor = z
    return menor

maior = maior(lista)
menor = menor(lista)

print('=-' *10)
print(f'voce digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(f'{c}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(f'{c}...', end='')
print()