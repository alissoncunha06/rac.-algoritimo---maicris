meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def pegar():
    while True:
        try:
            d = int(input("Insira o dia: "))
            m = int(input("Insira o mês: "))
            a = int(input("Insira o ano: "))
            return d, m, a
        except ValueError:
            print("Formato inválido")

def data(dia, mes, ano):
    nome_mes = meses[mes - 1]
    return f"{dia} de {nome_mes} de {ano}"

dia, mes, ano = pegar()
print(data(dia, mes, ano))