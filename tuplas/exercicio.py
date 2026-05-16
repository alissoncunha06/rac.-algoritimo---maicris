print()
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete","dezoito", "dezenove", "vinte")

while True:
  try:
    num = int(input("Insira um número de 0 a 20: "))
    if num < 0 or num > 20:
      print("Tente novamente")
    else:
      break
  except ValueError:
    print("formato inválido, tente novamente")
print()
print(f"Voce digitou o número {numeros[num]}")

print()