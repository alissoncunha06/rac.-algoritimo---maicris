print()
nomes = []
idades = []
alturas = []

for i in range(5):
    nome = input("Digite o nome: ")
    nomes.append(nome)
    while True:
        try:
            idade = int(input("Digite a idade: "))
            idades.append(idade)
            break
        except ValueError:
            print("Insira um valor válido para a idade.")
    while True:
        try:
            altura = int(input("Digite a altura em cm (ex: 175): "))
            alturas.append(altura)
            break
        except ValueError:
            print("Insira um valor válido para a altura.")

print("=-=" * 10, "DADOS COLETADOS", "=-=" * 10)

nomes.sort(reverse=True)
idades.sort(reverse=True)
alturas.sort(reverse=True)

for i in range(len(nomes)):
    print(f"{nomes[i]} - {idades[i]} anos - {alturas[i]} cm de altura")