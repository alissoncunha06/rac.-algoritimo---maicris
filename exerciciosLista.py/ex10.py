"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
"""
vetor1 = []
vetor2 = []

for i in range(10):
    while True:
        try:
            num1 = int(input("Digite um número inteiro para o vetor 1: "))
            vetor1.append(num1)
            break
        except ValueError:
            print("Entrada inválida, tente novamente.")

for i in range(10):           
    while True:
        try:
            num2 = int(input("Digite um número inteiro para o vetor 2: "))
            vetor2.append(num2)
            break
        except ValueError:
            print("Entrada inválida, tente novamente.")

vetor3 = []

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("=-=" * 10, "VETOR INTERCALADO", "=-=" * 10)
print(vetor3)
