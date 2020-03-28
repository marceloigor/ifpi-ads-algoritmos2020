# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada

# Entrada
nota1, peso1 = map(float, input('Digite dua 1º nota e o peso dela: ').split(','))
nota2, peso2 = map(float, input('Digite dua 2º nota e o peso dela: ').split(','))
nota3, peso3 = map(float, input('Digite dua 3º nota e o peso dela: ').split(','))

# Processamento
media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

# Saída
print(f'Média ponderada = {media_ponderada:.2f}')
