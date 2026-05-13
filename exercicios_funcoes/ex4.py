"""
Criar um programa que, fazendo uso de funções, cadastra
contatos em uma agenda telefônica, podendo excluir estes
contatos. Deve ser exibido um menu com as opções: inserir,
remover e sair.
"""
agenda = {}

def exibir_menu():
    pass

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
    

def remover_contatos():
    pass