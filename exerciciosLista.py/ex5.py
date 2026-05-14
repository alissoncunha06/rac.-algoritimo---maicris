print("=-=" * 50)
inteiros = []

for _ in range(10):    
    try:
        num = int(input("Digite um número inteiro: "))
        inteiros.append(num)
    except ValueError:
        print("Entrada inválida, insira um número inteiro.")
print()
def lista_pares(inteiros):
    pares = []
    impares = []
    for num in inteiros:
        if num % 2 == 0:
            pares.append(num)
        elif num % 2 != 0:
            impares.append(num)
    return pares, impares
numeros_pares, numeros_impares = lista_pares(inteiros)
print("=-=" * 50)
print(f"Na lista {inteiros} temos os seguintes números pares:")
for numero in numeros_pares:
    print(f"{numero}...", end="")
print()
print(f"E os seguintes números ímpares:")  
for numero in numeros_impares:
    print(f"{numero}...", end="")
print()
print("=-=" * 50)