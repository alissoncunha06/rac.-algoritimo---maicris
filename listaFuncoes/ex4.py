def argumento():
    while True:
        try:
            num = float(input("Insira um número: "))
            return num
        except ValueError:
            print("Formato inválido, insira um número")



def caractere(numero):
    if numero > 0:
        return "p"
    else:
        return "n"
    
numero = argumento()    
    
print(caractere(numero))