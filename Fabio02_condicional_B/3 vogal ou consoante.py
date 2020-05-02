# 3. Leia uma letra e verifique se a letra digitada é vogal ou consoante

def main():
    mensagem()

def mensagem():
    letra = input('Digite uma letra: ')

    vog_cons(letra)

def vog_cons(letra):
    if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u') \
        or (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
        print('Vogal')
    else:
        print('Consoante')
    



main()