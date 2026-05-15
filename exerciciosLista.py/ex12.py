"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos.
"""

alunos = []
dados = []

for _ in range(3):
  dados.append(str(input("Aluno: ")))
  while True:
    try:
      idade = int(input("Idade: "))
      dados.append(idade)
      break
    except ValueError:
      print("Formato inválido, tente novamente (ex: 15)")
    
  while True:
    try:
      altura = int(input("altura em cm (ex:180): "))
      dados.append(altura)
      break
    except ValueError:
      print("Formato inválido, tente novamente (ex: 180)")

alunos.append(dados[:])
dados.clear()

def media(alunos):
  altura = []
  for p in alunos:
    altura.append(p[1])
  return sum(altura) / len(altura)

media_altura = media(alunos)

# [0] é nome, [1] é idade e [2] é altura

for pessoa in alunos:
  if pessoa[1]

