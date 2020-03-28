# 21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

# Entrada
temperatura_f = int(input('Digite uma temperatura em °F: '))

# Processamento
temperatura_c = (5 * temperatura_f - 160) // 9

# Saída
print(f'{temperatura_f}°F é equivalente à {temperatura_c}°C')
