"""
Criar um programa que, fazendo uso de funções, cadastra
contatos em uma agenda telefônica, podendo excluir estes
contatos. Deve ser exibido um menu com as opções: inserir,
remover e sair.
"""
agenda = {}

def exibir_menu():
    print(10*"=", "MENU", 10*"=")
    print("1. Cadastrar Contato")
    print("2. Remover Contato")
    print("3. Sair")
    escolha = input("Insira o número de uma das opções acima: ")
    return escolha

def cadastrar_contatos():
    while True:
        nome = input("Digite o nome do contato (ou 0 para sair): ")
        if nome == "0":
            break
        try:
            telefone = int(input("Digite o telefone do contato com o codigo do país e área juntos, ex: 5541992419905: "))
            agenda[nome] = telefone
        except ValueError:
            print("Número inválido")
    
escolha = 

def remover_contatos():
    pass
while True:
    if escolha == 1:
        cadastrar_contatos()
    elif escolha == 2:
        remover_contatos()
    elif escolha == 3:
        break
    else:
        print("Hum, algo de errado aconteceu")
