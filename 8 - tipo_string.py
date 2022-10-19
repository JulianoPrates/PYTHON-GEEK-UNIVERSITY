"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre áspas simples -> 'uma string', '234', 'True'
- Estiver entre áspas duplas  -> "uma string", "234", "True"
- Estiver entre áspas simples triplas -> '''uma string''', '''234''', '''True'''

print(' ')
nome = 'Geek University'
print(nome, type(nome))

print('------------------------')

nome = "Ginas's Bar"
print(nome, type(nome))

print('------------------------')

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print('------------------------')

nome = 'Angelina
Jolie'
print(nome)

nome = 'Geek University'
print(nome.upper())

nome = 'Geek University'
print(nome.lower())

nome = 'Geek University'
print(nome.split()) # Transforma em uma lista de strings



"""
# - Estiver entre áspas duplas triplas -> """uma string""", """234""", """True"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University é o melhor curso'
print(nome[0:4])  # Slice de string
print(nome[5:15])  # Slice de string
print(nome.split())  # Separa a frase em lista
print(nome.split()[4])  # Pega a quinta palavra da lista do split
print(nome[::-1])  # Do primeiro elemento ao último e inverter
print(nome.replace('G', 'P'))  # Substituindo letras

print('---------------------------------------------------')

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)
print(texto[::-1])
