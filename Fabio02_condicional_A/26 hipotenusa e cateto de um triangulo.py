# 26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos

def main():
    mensagem()

def mensagem():
    a = int(input('Digite o lado A: '))
    b = int(input('Digite o lado B: '))
    c = int(input('Digite o lado C: '))

    maior(a, b, c)

def maior(a, b, c):
    if a > b and a > c:
        valor_hipotenusa(a, b, c)
    elif b > a and b > c:
        valor_hipotenusa(b, a, c)
    elif c > a and c > b:
        valor_hipotenusa(c, a, b)
    else:
        print('Os valores dos lados não formam um triângulo retângulo.')
        return mensagem()

def valor_hipotenusa(a, b, c):
    hipotenusa = a ** 2
    if (b ** 2 + c ** 2) == hipotenusa:
        print(f'{a} é a hipotenusa enquanto {b} e {c} são os catetos.')
    else:
        print('Os valores não formam um triângulo retângulo.')
        return mensagem()
    

main()
