"""
25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
uma mensagem de permissão de acesso ou não.
"""

def main():
    mensagem()

def mensagem():
    senha = int(input('Digte a senha: '))

    validar_senha(senha)

def validar_senha(senha):
    if senha == 1234:
        print('Acesso permitido.')
    else:
        print('Acesso negado.')
        return mensagem() 


main()
