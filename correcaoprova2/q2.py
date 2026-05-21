def get_user_data(users:dict):
    cpf = input("Digite o cpf: ")
    nome = input("Digite o nome: ")
    idade = int("Digite a idade :")
    telefones = []
    while True:
        fone = input("Digite o telefone: ")
        if fone == "":
            break
        telefones.append(fone)

    user = {"nome": nome, "Idade": idade, "Telefones": telefones}
    users[cpf] = user

    return cpf, user

    