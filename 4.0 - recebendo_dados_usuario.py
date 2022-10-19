"""
Recebendo dados do usuário

input() -> Todo tipo de dado recebido via input é do tipo string

Em Python tudo o que estiver entre:
- Aspas simples -> 'Angelina Jolie';
- Aspas duplas -> "Angelina Jolie";
- Aspas simples triplas -> '''Angelina Jolie''';
"""
# - Aspas duplas triplas -> """Angelina Jolie""";

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()
# ou
# nome = input('Qual seu nome? ')

# print('Seja bem-vindo(a) %s' % nome) -> Exemplo de print 'antigo' da v2.x
# print('Seja bem-vindo(a) {0}'.format(nome)) -> Exemplo de print 'moderno' a partir da v3.x
# print(f'Seja bem-vindo(a) {nome}') -> Exemplo de print mais atual a partir da v3.7

# print("Qual a sua idade?")
# idade = input()
# ou
# idade = input('Qual a sua idade? ')

# print('O(a) %s tem %s anos' % (nome, idade)) -> Exemplo de print 'antigo' da v2.x
# print('O(a) {0} tem {1} anos'.format(nome, idade)) -> Exemplo de print 'moderno' a partir da v3.x
# print(f'O(a) {nome} tem {idade} anos') -> Exemplo de print mais atual a partir da v3.7

nome = input('Qual seu nome? ')

print(f'Seja bem-vindo(a) {nome}')

idade = int(input('Qual a sua idade? '))

print(f'O(a) {nome} tem {idade} anos')

# int(idade) -> é um cast
# Cast é a 'conversão' de um tipo de dado para outro
# print(f'O(a) {nome} nasceu em {2020 - int(idade)}')

print(f'O(a) {nome} nasceu em {2020 - idade}')
