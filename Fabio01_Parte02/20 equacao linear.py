# 20. Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo: Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y. (pdf)

# Entrada
a = float(input('Digite o valor do coeficiente de a: '))
b = float(input('Digite o valor do coeficiente de b: '))
c = float(input('Digite o valor do coeficiente de c: '))
d = float(input('Digite o valor do coeficiente de d: '))
e = float(input('Digite o valor do coeficiente de e: '))
f = float(input('Digite o valor do coeficiente de f: '))

# Processamento
x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

# Saída
print(f'X = {x} \nY = {y}')
