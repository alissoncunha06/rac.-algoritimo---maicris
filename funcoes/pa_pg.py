"""
usar recursividade para calcular o n-ésimo termo da PA
"""
def pa(a, r, n):
    if n == 1:
        return a
    return r + pa(a, r, n - 1)

a = (int(input("Digite o primeiro termo da PA: ")))
r = (int(input("Digite a razão da PA: ")))
n = (int(input("Digite o n-ésimo termo que deseja calcular: ")))
an = pa(a, r, n)
print(f"O {n}-ésimo termo da PA é {an}")