import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2


primeira = lancar_dados()
print(f"Você tirou {primeira}")

if primeira in (7, 11):
    print("Natural, você ganhou")
elif primeira in (2, 3, 12):
    print("Craps, você perdeu")
else:

    ponto = primeira
    print(f"Seu Ponto é {ponto}. Continue jogando até tirar {ponto} de novo (ou 7 pra perder).")
    
    while True:
        nova = lancar_dados()
        print(f"Você tirou {nova}")
        
        if nova == ponto:
            print("Você tirou o Ponto, ganhou")
            break
        elif nova == 7:
            print("Tirou 7, perdeu")
            break