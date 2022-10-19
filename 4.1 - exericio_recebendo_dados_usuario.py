"""
nome = input('Qual seu nome? ')
print(f'Seja Bem-Vindo(a) {nome} ')
idade = int(input('Qual sua idade? '))
print(f'O(a) {nome} tem {idade} anos ')
print(f'O(a) {nome} nasceu em {2020 - idade}')
print('Parabéns, você completou a parte de entrada de dados do curso de Python! ')
"""
print('-----')
print('SITES')
print('-----')

print()

print('Alok')
print('Vintage Culture')
print('MEDUZA')

print()

escolha_site = str(input('Escolha qual música deseja acessar: '))
# Forma 1
if escolha_site == 'Alok':
    print('https://open.spotify.com/album/1jU9kFRQP9Vf7R5ncpkcCh?si=KwKi8VxLSmWnx2iOOVfF3g')
# Forma 2
elif escolha_site == 'Vintage Culture':
    import webbrowser
    webbrowser.open('https://open.spotify.com/track/49ifZncZRGpqKqx3B3DoSO?si=9wVYKSHxRLqF1cWV76Davw')

elif escolha_site == 'MEDUZA':
    import webbrowser
    webbrowser.open('https://open.spotify.com/track/6iW38RGqdDGOofmz2HeXLW?si=Hiacv7zPRrGqBTErOt_ZIw')

#  elif escolha_site == 'MEDUZA':
#  print('https://open.spotify.com/track/6iW38RGqdDGOofmz2HeXLW?si=Hiacv7zPRrGqBTErOt_ZIw')
