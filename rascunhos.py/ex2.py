lista = []
print('=-' * 20)
while True:
    try:
        num = float(input('digite um valor: '))
        if num not in lista:
            lista.append(num)
        else:
            print('valor duplicado, nao vou adicionar!')
    except ValueError:
        print('formato invalido, tente novamente')
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == 's':
        pass
    elif resposta == 'n':
        break
    elif resposta != 's' or resposta != 'n':
        print('hum, algo deu errado')
print('=-' * 20)
lista.sort()
print(f'voce inseriu os numeros {lista}')
print('=-' * 20)