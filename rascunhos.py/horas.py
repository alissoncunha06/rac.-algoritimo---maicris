def converter(horas, minutos):
    if horas == 0:
        return 12, minutos, "A"
    elif horas == 12:
        return 12, minutos, "P"
    elif horas > 12:
        return horas - 12, minutos, "P"
    else:
        return horas, minutos, "A"

def saida(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {periodo}.M.")

while True:
    while True:
        try:
            horas = int(input("Insira a hora: "))
            minutos = int(input("Insira o minuto: "))
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                break
            print("Hora deve ser 0-23 e minuto 0-59")
        except ValueError:
            print("Formato inválido, tente novamente")

    hora_conv, min_conv, periodo = converter(horas, minutos)
    saida(hora_conv, min_conv, periodo)

    resposta = input("Deseja converter outro horário? (s/n): ").lower()
    if resposta != "s":
        break