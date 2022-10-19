"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 2

range(valor_de_início, valor_de _parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Forma 4 (igual forma 3, mas inversa)

range(valor_de_início, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

"""
# Exemplo Forma 1
for num in range(11):
    print(num)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)

# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)

# Fazendo lista de um range (ou convertendo um range para uma lista)
lista = list(range(10))
print(lista)
