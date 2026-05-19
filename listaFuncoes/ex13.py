"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta
função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1
e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores
dentro da faixa de forma elegante.
"""

def desenhar(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    borda = "+" + "-" * colunas + "+"
    meio  = "|" + " " * colunas + "|"
    
    print(borda)
    for _ in range(linhas):
        print(meio)
    print(borda)

linhas = int(input("Quantas linhas? "))
colunas = int(input("Quantas colunas? "))
desenhar(linhas, colunas)