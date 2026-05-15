galera = list()
dado = list()
for c in range(3):
  dado.append(str(input("Nome: ")))
  dado.append(int(input("Idade: ")))
  galera.append(dado[:])


print(galera)
