print('=-' * 20)
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def contar(lista):
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista2 = []
    contador = 0
    for i in lista:
        if i in vogais:
            contador += 1
            lista2.append(i)
    return contador, lista2

contador, vogais_encontradas = contar(lista)
print(f'Na lista {lista} existem {contador} vogais: {vogais_encontradas}')
print('=-' * 20)