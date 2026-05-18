def soma(a, b, c):
    return a + b + c

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Formato inválido, insira uma int")

n1 = ler_inteiro("Insira o primeiro número: ")
n2 = ler_inteiro("Insira o segundo número: ")
n3 = ler_inteiro("Insira o terceiro número: ")

print(soma(n1, n2, n3))