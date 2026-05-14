notas = [
    [8, 7, 9, 6],
    [6, 5, 7, 8],
    [10, 9, 8, 9],
]

for i in range(len(notas)):
    soma = 0
    for j in notas[i]:
        soma += j
    print(f"Aluno {i+1}: soma das notas = {soma}")