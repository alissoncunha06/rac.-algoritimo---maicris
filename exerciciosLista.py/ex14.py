"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente"
"""
print()
perguntas = [
  "Telefonou para a vítmia?", 
  "Esteve no local da vítima?", 
  "Mora perto da vítima?", 
  "Devia para a vítmia?", 
  "Já Trabalhou com a vítima?",
]
respostas = []

for pergunta in perguntas:
  while True:
    resp = input(f"{pergunta} (s/n): ")
    if resp in ("s", "n"):
      respostas.append(resp)
      break
    print("Sigite s ou n")

contador = 0

for resposta in respostas:
  if resposta == "s":
    contador += 1

if contador == 0:
  print("Pessoa é inocente")
elif contador == 2:
  print("Pessoa Suspeita")
elif contador == 3 or contador == 4:
  print("Pessoa é cúmplice")
else:
  print("Pessoa é assasina")
print()