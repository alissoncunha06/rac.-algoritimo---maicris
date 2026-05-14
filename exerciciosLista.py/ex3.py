print('=-' * 20)
notas = []
while True:
    try:
        for i in range (4):
            num = float(input('Insira a nota: '))
            notas.append(num)
        break
    except ValueError:
        print('formato invalido, tente novamente') 

def media(notas):
    return sum(notas) / len(notas)

media_notas = media(notas)
print('As notas inseridas foram: ', end='')
for v in notas:
    print(f'{v:.2f},', end=' ')
print(f'. A média das notas é: {media_notas:.2f}')
print('=-' * 20)
