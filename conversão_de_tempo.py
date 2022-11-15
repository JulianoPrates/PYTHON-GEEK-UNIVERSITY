N = int(input())

def convert(segundos):
    segundos = N %  60
    hora =  N // 3600
    minutos = ( N % 3600 ) // 60
    print(f"{hora}:{minutos}:{segundos}")

convert(N)
