# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
while True:
    try:
        num = int(input("Insira um número inteiro: "))
        break
    except ValueError:
        print("Formato inválido")

def contar(num):
    return len(str(abs(num)))

print(f"A quantidade de dígitos é {contar(num)}")