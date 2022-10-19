"""
Estruturasa condicionais
if (se), else (senão), elif (else if)

# Estrutura condicional if, else em C
exemplo:
if(idade < 18){
    printf("Menor de idade");
}else if(idade == 18){
  printf("Tem 18 anos");
}else{
  printf("Maior de idade");
}

# Estrutura condicional if, else em Java
exemplo:
if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
  System.out.println("Tem 18 anos");
}else{
  System.out.println("Maior de idade");
}

"""
idade = 20

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 20:
    print('Tem 20 anos')
else:
    print('Maior de idade')

print('-----------------------------')

# TESTE COM SUCESSO
idade = int(input('Quantos anos você tem? '))
if idade < 18:
    print('você está chegando lá!')
elif idade == 18:
    print('Você tem 18 anos')
else:
    print('Parabéns, você já pode dirigir!')
