vetor = []

for i in range(10):
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
        linha.append(num * num)
    return linha
quadrados = conta(vetor)

def somar(quadrados):
    soma = 0
    for num in quadrados:
        soma += num
    return soma

soma_quadrados = somar(quadrados)
print("=-=" * 10, "QUADRADOS DOS NÚMEROS", "=-=" * 10)
print(quadrados)

print("=-=" * 10, "SOMA DOS QUADRADOS", "=-=" * 10)
print(f"Soma dos quadrados: {soma_quadrados}")

