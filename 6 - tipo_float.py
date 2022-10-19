"""
Tipo Float (real, decimal)
Com casas decimais
OBS: o separador de casas decimais na programação
é o ponto e não vírgula.
"""
# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

print('____________________')
print(' ')
# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

print('____________________')
print(' ')
# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1, type(valor1))
print(valor2), print(type(valor2))

print('____________________')
print(' ')
# Podemos converter um Float para um int
"""
OBS: Ao converter um FLoat para um inteiro, nós perdemos precisão
"""
res = int(valor)
print(res, type(res))

print('____________________')
print(' ')
# Podemos converter um inteiro para Float
num = 1_000
print(num, type(num))
print(float(num), '<class float>')

print('____________________')
print(' ')
# Podemos trabalhar com números complexos
variavel = 5j
print(variavel, type(variavel))