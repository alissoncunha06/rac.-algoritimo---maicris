print("=-=" * 10, "SISTEMA", "=-=" * 10)
aluno = {}
aluno["Nome"] = (input("Nome do aluno: "))
while True:
  try:
    aluno["Média"] = float(input(f"Média de {aluno["Nome"]}: "))
    break
  except ValueError:
    print("Formato inválido, tente novamente")

if aluno["Média"] >= 7:
  aluno["Situação"] = "Aprovado"
else:
  aluno["Situação"] = "Reprovado"
print("=-="*10, "STATUS", "=-=" * 10)
for k, v in aluno.items():
  print(f"{k}: {v}")


print("=-=" * 20)