"""
Loop for

loop -> Estrutura de repetição
For -> É uma dessas estruturas

C ou Java:
for(int i = 0; i < 10; i++){
    //execução do loop
}

Python:
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
 - String
    nome = 'Geek University'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor inicial, valor final)
OBS: O valor final não é inclusivo. Se colocar 10 de valor final, vai imprimir somente 9.
range(1, 4)
1
2
3
4 não pega

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(nome(indice))

for indice, letra in enumerate(nome):
    print(nome(letra))

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for valor in enumerate(nome):
    print(valor)

===============================================================================
Dica:
qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

Dica:
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n} valor de {qtd}: '))
    soma = soma + num
print(f'A soma é {soma}')

Dica:
nome = 'Geek University'
for letra in nome:
    print(letra, end='')  # imprime nome sem pular linha

Tabela de Emojis Unicode:  https://www.unicode.org/emoji/charts/full-emoji-list.html

# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

"""
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n} valor de {qtd}: '))
    soma = soma + num
print(f'A soma é {soma}')