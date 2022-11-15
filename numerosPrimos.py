# N = int(input())

# for i in range(0, N):
#     if ( N % i == 0 ):
#         print(N, " eh primo")
#     else:
#         print(N, "nao eh primo")


n = int(input())

for i in range(0,n):
    num = int(input())
    s = 0
    j = 1
    while j <= num:
        if num % j == 0:
            s = s + 1
        j = j + 1
    if s > 2:
        print(f"{num} nao eh primo")
    else:
        print(f"{num} eh primo")
