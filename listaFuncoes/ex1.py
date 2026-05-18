while True:
    try:
        num = int(input("Insira um número int: "))
        break
    except ValueError:
        print("Formato inválido, insira uma int")

def main(num):
    for i in range(num):
        for j in range(i + 1):
            print(num, end=" ")
        print()
main(num)