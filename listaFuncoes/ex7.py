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
            valor = float(input("Qual é o valor da prestação?(0 para sair) "))
            if valor < 0:
                print("Valor n pode ser menor que zero")
            else:
                return valor
        except ValueError:
            print("formato inválido")

def atraso():
    while True:
        atraso = input("A prestação está atrasada? (s/n) ").lower()
        if atraso == "s":
            return True
        elif atraso == "n":
            return False
        else:
           print("Digite s ou n") 
       
def dias(prazo):
    if prazo:
        while True:
            try:
                dias = int(input("Em quantos dias está atrasada? "))
                if dias <= 0:
                    print("Dias não pode ser negativo ou zero")
                else:
                    return dias
            except ValueError:
                print("Formato inválido")
    else:
        return 0

#calcular o valor a ser pago
"""
- Para pagamentos sem atraso, cobrar o valor da prestação
- Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso
"""
def valorPagamento(valor1, prazo, dias1): #recebe parametro info do usuario
    if not prazo:
        return valor1
    else:
        return valor1 + (valor1 * 0.03) + (valor1 * 0.001 * dias1)

#fazer rodar infinitamente até o usuário digitar 0   

quantidade = 0 #acumuladores pro relatório do coisa
total = 0 

while True:
    valor1 = prestacao()

    #0 para sair
    if valor1 == 0:
        break

    prazo = atraso()
    dias1 = dias(prazo)

    valor_pago = valorPagamento(valor1, prazo, dias1)
    #mostrar o valor
    print(f"Valor a pagar R${valor_pago:.2f}")
    quantidade += 1
    total += valor_pago

#exibir relatória com quantidade e o valor total de prestacoes pagas no dia

print(f"\nRelatório do dia:")
print(f"Quantidade de prestações: {quantidade}")
print(f"Valor total de prestações: R${total:.2f}")