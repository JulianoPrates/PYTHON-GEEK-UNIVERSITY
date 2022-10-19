"""
Estruturas lógicas: and, or, not, is

Operadores unários:
   - not
Operadores binários:
   - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True.
Para o 'or', um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for False vira True, se for True vira False.
Para o 'is', o valor é comparado com um segundo valor.
"""
print(' ')
print('1)')
ativo = False
logado = True

if ativo and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Favor checar seu e-mail')

print('---------------------------------------------------------------')
print('2)')
ativo = False
logado = True

if ativo or logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Favor checar seu e-mail')

print('---------------------------------------------------------------')
print('3)')
ativo = True
logado = True

if not ativo:
    print('Você precisa ativar sua conta. Favor checar seu e-mail')
else:
    print('Bem-vindo usuário')

print('---------------------------------------------------------------')
print('4)')
ativo = False
logado = True

if ativo is False:
    print('Você precisa ativar sua conta. Favor checar seu e-mail')
else:
    print('Bem-vindo usuário')
