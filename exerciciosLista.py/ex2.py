print('=-' * 20)
lista = []
while True:
    try:
        for i in range (10):
            num = float(input('Insira um numero real: '))
            lista.append(num)
        break
    except ValueError:
        print('formato invalido, tente novamente') 

lista.sort(reverse=True)
print(lista)
print('=-' * 20)