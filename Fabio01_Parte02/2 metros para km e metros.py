# Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

# Entrada
metros = int(input('Digite um valor em metros: '))

# Processamento
km = metros // 1000
metro =  (metros % 1000)

# Saída
print(f'{metros} m é equivalente a {km} km e {metro} m')