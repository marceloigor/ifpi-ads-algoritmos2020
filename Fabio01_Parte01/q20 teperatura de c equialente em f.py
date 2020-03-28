# 20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

# Entrada
temperatura_c = int(input('Digite uma temperatura em °C: '))

# Processamento
temperatura_f = (9 * temperatura_c + 160) // 5

# Saída
print(f'{temperatura_c}C° é equivalente à {temperatura_f}F°')
