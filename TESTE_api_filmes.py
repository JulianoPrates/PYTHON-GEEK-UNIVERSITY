import requests
import json

dicionario = json.loads(requests.get)
def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo)
        dicionario = json.loads(requests.get)
        return dicionario
    except:
        print('Erro na conexão')
        return None

def printar_detalhes(filme):
    print('Título:', dicionario['Title'])
    print('Ano:', dicionario['Year'])
    print('Diretor:', dicionario['Director'])
    print('Atores:', dicionario['Actors'])
    print('Nota:', dicionario['imdbRating'])

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == False:
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)
2