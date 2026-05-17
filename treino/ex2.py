def somar(lista):
  caixa = 0
  for valor in lista:
    caixa += valor
  return caixa

def main():
  lista = [10, 20, 30, 40]
  print(somar(lista))

main()