# 17. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos
# que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

# Entrada
idade_fuma = int(input('Dígite o número de anos que fuma: '))
numero_cigarro_dia = int(input('Dígite o números de cigarro que você fuma por dia: '))
preco_carteira_cigarro = float(input('Digite o valor da carteira de cigarros: '))

# Processamento
valor_unitario = preco_carteira_cigarro / 20
valor_gasto_cigarros = (valor_unitario * numero_cigarro_dia) * (idade_fuma * 365)

# Saída
print(f'O Valor gasto em cigarros foi de R$ {valor_gasto_cigarros:.2f}')
