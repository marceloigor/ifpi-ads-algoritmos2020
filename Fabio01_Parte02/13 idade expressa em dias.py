# 13. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

# Entrada
anos = int(input("Digite uma idade em anos: "))
meses = int(input("Digite uma idade em meses: "))
dias = int(input("Digite uma idade em dias: "))

# Processamento
dia = (anos * 365) + (meses * 30) + dias

# Saída
print(f'{dia} dias')
