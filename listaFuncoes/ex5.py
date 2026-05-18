def custo():
    while True:
        try:
            custo = float(input("Insira o custo INICIAL do produto, ou seja, sem imposto: "))
            if custo < 0:
                print("O valor deve ser maior que zero")
            else:
                return custo
        except ValueError:
            print("Formato inválido")

def taxaimposto():
    while True:
        try:
            imposto = float(input("Insira, em porcentagem (ex: 0.15 para 15%), o imposto: ")) #arrumar aqui, pedir o imposto normal e dividir por 100 dentro da funcao
            if imposto < 0:
                print("Deve ser acima de 0")
            else:
                return imposto
        except ValueError:
            print("Formato inválido")

valor = custo()
taxa = taxaimposto()

def somaimposto(valor, taxa):
    return (valor + (valor * taxa))

valorfinal = somaimposto(valor, taxa)

print(f"O valor inicial é {valor}, após o imposto de {taxa * 100}% o valor final é {valorfinal}")