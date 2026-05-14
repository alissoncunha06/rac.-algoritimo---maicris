lista = []
while True:
    try:
        for i in range (5):
            num = int(input('Insira um numero inteiro: '))
            lista.append(num)
        break
    except ValueError:
        print('formato invalido, tente novamente') 

print(lista)   