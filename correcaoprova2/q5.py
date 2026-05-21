import math #nn precisa do import na prova

def area_base_circulo(raio):
    return math.pi * raio ** 2

def comprimento_base_circulo(raio):
    return 2 * math.pi * raio

def area_cilindro(altura, raio):
    return 2 * area_base_circulo(raio) + altura * comprimento_base_circulo(raio)

altura = float("Insira a altura ")
raio = float("insira o raio: ")

area = area_cilindro(raio, altura)
print("A área do cilindro é", raio)