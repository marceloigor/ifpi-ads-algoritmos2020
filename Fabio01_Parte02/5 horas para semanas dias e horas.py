# 5 Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

# Entrada
horas = int(input('digite um valor em horas: '))

# Processamento
semanas = horas // 168
dias = horas // 24
hora = horas % 60

# Saída
print(f'{horas} horas é equivalente à {semanas} semanas {dias} dias {hora} horas')
