"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127
-> 721
"""
print()
while True:
    try:
        num = int(input("Insira um número inteiro: "))
        break
    except ValueError:
        print("Formato inválido, tente novamente")

def inverter(num):
    caixa = ""
    for digito in str(abs(num)): #for digito in str(abs(num)):
        caixa = digito + caixa
    return caixa

print(f"O número invertido é {inverter(num)}")

print()