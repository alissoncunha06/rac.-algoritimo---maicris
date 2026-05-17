#dicionário
estoque = {
  "Pão": 10, "Hamburguer": 12, "Tomate": 5, "Bacon": 5, "Ovo": 5
}

cardapio = {
  "X-Burguer": ["Pão", "Hamburguer"],
  "X-Salada": ["Pão", "Hamburguer", "Tomate"], 
  "X-Bacon": ["Pão", "Hamburguer", "Tomate", "Bacon"], 
  "X-Egg": ["Pão", "Hamburguer", "Ovo"],
  "X-Tudo": ["Pão", "Hamburguer", "Tomate", "Hamburguer", "Bacon", "Ovo"]
}
def imprimir_cardapio(cardapio):
  print("=-="*10, "MENU", "=-="*10)
  contador = 1
  for comida in cardapio:
    ingredientes = ", ".join(cardapio[comida])
    print(f"{contador}: {comida} - {ingredientes}")
    contador += 1

def verificar_estoque(estoque, ingredientes):
  faltantes = []
  for ingrediente in ingredientes:
    quantidade_necessaria = ingredientes.count(ingrediente)
    if estoque[ingrediente] < quantidade_necessaria:
      faltantes.append(ingrediente)
  return faltantes

def executar_pedido():
  pass

def main():
  while True:
    pergunta = input("O que você deseja pedir? ")
    if pergunta == "0":
      break
    elif pergunta not in cardapio:
      print("Item não encontrado")
    else:
      pass #chamar funcao pra executar o pedido
    imprimir_cardapio(cardapio)#1. mostrar o cardapio
    #2. Perguntar o pedido e 0 pra sair
    #3. Verificar se o item está no cardapio e avisar
    #4. Se existir no cardápio, tentar preparar
    #5. repetir

main()