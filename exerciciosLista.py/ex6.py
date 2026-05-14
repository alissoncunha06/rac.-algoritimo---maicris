nomes = [] #criar a lista de nomes
notas = [] #criar a lista de notas (que vai ser uma matriz)

for i in range(10): #repete tudo que está dentro desse for 10 vezes
    nome = input("Insira o nome do aluno: ") #pega o nome do aluno 
    nomes.append(nome) #coloca o nome desse aluno na lista nomes

    linha = [] #criar essa lista (a matriz) que vai ir dentro de outra da lista notas
    for j in range(4): #repetir 4 vezes pra pegar 4 notas do aluno acima
        nota = float(input(f"Insira a nota {j+1} do aluno: ")) #j+1 pra n ficar "insira a nota 0, mas sim "Insira a nota 1"
        linha.append(nota) #coloca a nota em linha pra ter as 4 notas daquele respectivo aluno

    notas.append(linha) #pega essa lista com 4 notas de UM aluno e joga na lista notas, formanod a matriz

for i in range(len(nomes)): #percorrer cada aluno, i = 0 -> o aluno no index 0 e vai acessar a sua lista de notas, que tem a lista linhas dentro com as 4 notas
    soma = 0
    for nota in notas[i]: #vai percorrer notas[i], ou seja, a linha daquele aluno, que tem as 4 notas, e vai pegar cada nota dessa linha 
        soma += nota
    media = soma / len(notas[i])
    print(f"{nomes[i]}: {notas[i]} - média: {media:.2f}")  