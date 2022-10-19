"""
Escopo de variáveis

Dois casos de scopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja,
    seu escopo compreende todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada

Para declarar variáveis em Python, fazemos:
 -> nome_da_variável = valor_da_variável

 Python é uma linguagem de tipagem dinâmica. Isso significa que
 ao declararmos uma variável, nós não colocamos o tipo de dado dela.
 Este tipo é inferido ao atribuirmos o valor à mesma.

 Exemplo em C:
 int numero = 42

 Exemplo em Java:
 int numero = 42

 Exemplo em Python:
 numero = 42

 numero = 42  # Exemplo de variável global
print(numero, type(numero))

numero = 'Geek'
print(numero, type(numero))
"""
numero = 2
novo = 0

if numero > 10:
    novo = numero + 10  # A variável 'novo'
    print(novo)
print(novo)
