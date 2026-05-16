print()
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for i in range(12):
    while True:
        try:
            temp = float(input(f"Insira a temperatura média de {meses[i]} em Celsius: "))
            temperaturas.append(temp)
            break
        except ValueError:
            print("Formato inválido")

def calcular_media(temperaturas):
    return sum(temperaturas) / len(temperaturas)

media = calcular_media(temperaturas)
print(f"\nA média anual é de {media:.1f}°C\n")

# Lista de tuplas (mês, temperatura)
acima = []
for i, temp in enumerate(temperaturas):
    if temp > media:
        acima.append((meses[i], temp))   # ← guarda os dois juntos

if not acima:
    print(f"Nenhum mês ficou acima da média de {media:.1f}°C")
else:
    print("Meses acima da média:")
    for mes, temp in acima:              # ← desempacota a tupla
        print(f"  {mes} ({temp:.1f}°C)")