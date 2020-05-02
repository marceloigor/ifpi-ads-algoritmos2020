# 2. Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

def main():
    mensagem()

def mensagem():
    letra = input('Digite uma letra: ')

    f_m(letra)

def f_m(letra):
    if letra == 'f' or letra == 'F':
        print('Sexo Feminino')
    elif letra == 'm' or letra == 'M':
        print('Sexo Masculino')
    else:
        print('Sexo Inválido')
        return mensagem()
        

main()