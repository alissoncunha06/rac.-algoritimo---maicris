"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
print()
meses = ["Janeiro", "fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for i in range(12):
  while True:
    try:
      temp = float(input(f"Insira a temperatuda média de {meses[i]} em Célcius: "))
      temperaturas.append(temp)
      break
    except ValueError:
      print("Formato inválido")
print()
print(temperaturas) #checar apenas - debug
print()
def calcular_media(temperaturas):
  return sum(temperaturas) / len(temperaturas)

media = calcular_media(temperaturas)
print()
print(media) #checar- debug
print()
meses_acima = []

for i in range(len(meses)):
  if temperaturas[i] > media:
    meses_acima.append(meses[i])

print(meses_acima)
print()