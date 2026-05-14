"""
copia a lista a para a lista b, sem isso b seria uma referência para a
lista a, ou seja, se eu mudar um valor em b, ele mudaria o valor em a também
"""
a = [2, 3, 4, 7]
b = a[:] 
b[2] = 10

print(f'Lista A: {a}')
print(f'Lista B: {b}')