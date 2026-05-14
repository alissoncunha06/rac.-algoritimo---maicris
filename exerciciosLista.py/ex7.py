print()
lista = []

for i in range(5):
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            lista.append(num)
            break
        except ValueError:
            print("Entrada inválida.")
print()
print("=-=" * 10, "LISTA DE NÚMEROS", "=-=" * 10)
print(lista)
print("=-=" * 10, "SOMA DOS NÚMEROS", "=-=" * 10)
soma = 0
for numeros in lista:
    soma += numeros
print(f"Soma dos números: {soma}")
print("=-=" * 10, "MULTIPLICAÇÃO DOS NÚMEROS", "=-=" * 10)
multi = 1
for numeros in lista:
    multi *= numeros
print(f"Multiplicação dos números: {multi}")
print()