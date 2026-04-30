'''
 Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''
ponto1 = 0
ponto2 = 0
pontos = int(input('escolha a quantidade de pontos para acabar o jogo: '))
while ponto1 + ponto2 < pontos or ponto1 == ponto2:
    pl1 = input('Jogador 1 escolha entre pedra, papel e tesoura: ')
    pl2 = input('Jogador 2 escolha entre pedra, papel e tesoura: ')
    if pl1 == pl2:
        print('empate')
    elif pl1 == 'pedra' and pl2 == 'tesoura':
        ponto1 += 1
        print('ponto para pl1')
    elif pl1 == 'papel' and pl2 == 'pedra':
        ponto1 += 1
        print('ponto para pl1')
    elif pl1 == 'tesoura' and pl2 == 'papel':
        ponto1 += 1
        print('ponto para pl1')
    else:
        print('ponto para pl2')
        ponto2 += 1
print("Placar final:")
print("Jogador 1:", ponto1)
print("Jogador 2:", ponto2)