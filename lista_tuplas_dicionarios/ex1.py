#dicionário
estoque = {
  "Pão": 10, "Hamburguer": 12, "Tomate": 5, "Bacon": 5, "Ovo": 5
}

cardapio = {
  "X-Burguer": ["Pão", "Hamburguer"],
  "X-Salada": ["Pão", "Hamburguer", "Tomate"], 
  "X-Bacon": ["Pão", "Hamburguer", "Tomate", "Bacon"], 
  "X-Egg": ["Pão", "Hamburguer", "Ovo"],
  "X-Tudo": ["Pão", "Hamburguer", "Tomate", "Hamburguer", "Bacon", "ovo"]
}

print("=-="*15, "MENU", "=-="*15)

def imprimir_cardapio(cardapio):
  numero = 1
  for comida in cardapio:
    ingredientes = ", ".join(cardapio[comida])
    print(numero, "-", comida, "->", ingredientes)
    numero = numero +1
imprimir_cardapio(cardapio)

def pedir_msg():
  while True:
    pergunta= int(input("O que deseja pedir? "))
    if pergunta = "0":
      break
    elif pergunta not in cardapio:
      print("Item não localizado no cardápio")
      #terminar o codigo pra chamar o pedido dentro do cardapio

 