"""
21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
contrario, é arredondado para o inteiro imediatamente inferior.
"""

def main():
    numero = float(input('Digite um valor: '))

    arredondamento(numero)

def arredondamento(numero):
    fracionario = numero - int(numero)

    if fracionario >= 0.5:
        arredondado = numero + (1 - fracionario)
        print(arredondado)
    else:
        arredondado = numero - fracionario
        print(arredondado)


main()
