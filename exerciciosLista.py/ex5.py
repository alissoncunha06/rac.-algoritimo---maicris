inteiros = []

while True:
    for _ in range(10):    
        try:
            num = int(input("Digite um número inteiro: "))
            inteiros.append(num)
        except ValueError:
            print("Entrada inválida, insira um número inteiro.")

            