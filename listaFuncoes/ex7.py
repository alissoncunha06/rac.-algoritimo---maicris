"""
-determinar o valor a ser pago por uma prestação de
uma conta

-Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso.
"""

# info do usuario aqui
    #valor da prestacao
    #numero de dias em atraso
def prestacao():
    while True:
        try:
            valor = float(input("Qual é o valor da prestação? "))
            return valor
        except ValueError:
            print("formato inválido")

valor1 = prestacao()

def atraso():
    while True:
        atraso = input("A prestação está atrasada? (s/n) ").lower()
        if atraso == "s":
            return True
        elif atraso != "n":
            print("Digite s ou n")
        else:
            return False

prazo = atraso() 
       
def dias(prazo):
    if prazo == True:
        while True:
            try:
                dias = int(input("Em quantos dias está atrasada? "))
                return dias
            except ValueError:
                print("Formato inválido")

dias1 = dias(prazo)

#calcular o valor a ser pago
"""
- Para pagamentos sem atraso, cobrar o valor da prestação
- Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso
"""
def valorPagamento(valor1, prazo, dias1): #recebe parametro info do usuario
    if prazo == False:
        return valor1
    else:
        return (valor1 + (valor1 * 0.03) + (0.01 * dias1))
    



#exibir o valor a ser pago

#solicitar se o usuario quer calcular outra coisa ou 0 para sair

#exibir relatória com quantidade e o valor total de prestacoes pagas no dia