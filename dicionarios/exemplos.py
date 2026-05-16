print()
estado = dict()
brasil = list()
for c in range(3):
  estado["UF"] = str(input("Unidade federativa: "))
  estado["Sigla"] = str(input("Sigla do Estado: "))
  brasil.append(estado.copy()) #é importante fazer o copy
for e in brasil:
  for k, v in e.items():
    print(f"O campo {k} tem valor {v}")
print()