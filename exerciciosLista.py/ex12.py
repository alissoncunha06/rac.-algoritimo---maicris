"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos.
"""

alunos = []
dados = []

dados.append(str(input("Aluno: ")))
while True:
  try:
    idade = int(input("Idade:"))
    dados.append(idade)
  except ValueError:
    print("Formato inválido, tente novamente (ex: 15)")

alunos.append(dados[:])
dados.clear()

def media(alunos):
  altura = []
  for i in alunos:
    altura.append(i[1])
  return sum(altura) / len(altura)

media_altura = media(alunos)

for pessoa in alunos:
  if pessoa[1] < media_altura:
    print(f"Aluno {aluno[0]} tem altura inferior a média {media_altura}")
