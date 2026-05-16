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
lista = []
while True:
  contato = input("Telefonou para a vítima? (s/n): ")
  if contato == "s" or contato == "n":
    lista.append(contato)
    break
  else:
    print("Digite s ou n")

while True:
  local = input("Esteve no local do crime? (s/n): ")
  if local =="s" or local == "n":
    lista.append(local)
    break
  else:
    print("Digite s ou n")

while True:
  morar = input("Mora perto da vítima? (s/n): ")
  if morar == "s" or morar == "n":
    lista.append(morar)
    break
  else:
    print("Digite s ou n")

while True:
  dever = input("Devia para a vítima? (s/n): ")
  if dever == "s" or dever == "n":
    lista.append(dever)
    break
  else:
    print("Digite s ou n")

while True:
  trabalhar = input("Já trabalhou com a vítima? (s/n): ")
  if trabalhar == "s" or trabalhar == "n":
    lista.append(trabalhar)
    break
  else:
    print("Digite s ou n")

contador = 0

for resposta in lista:
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