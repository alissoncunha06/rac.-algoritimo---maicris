vetor = []

for i in range(2):
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            vetor.append(num)
            break
        except ValueError:
            print("Entrada inválida, tente novamente.")

print("=-=" * 10, "VETOR DE NÚMEROS", "=-=" * 10)
print(vetor)

def conta(vetor):
    linha = []
    for num in vetor:
        