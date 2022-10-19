"""
Tipo Booleano
Algebra Booleano, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula
"""
print('1)')
ativo = True
print(ativo, type(ativo))
print('---------------------')

# OPERAÇÕES BÁSICAS

# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print('2)')
print(not ativo, type(ativo))
print('---------------------')

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores.
Ou um ou outros deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print('3)')
logado = False
print(ativo or logado, type(ativo), type(logado))
print('---------------------')

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
print('4)')
num1, num2 = 7, 8
print(num1 < num2 or num1 > 3)
print(num1 < num2 and num1 > 3)
