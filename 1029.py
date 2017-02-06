#variaveis
Chama = 0

# subprogramas
def SegFib(n):
    global Chama
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        Chama = Chama+1
        return SegFib(n-1) + SegFib(n-2)

#programa principal
cont = int(input())
i = 1

while (i <= cont):
    x = int(input())
    print('fib(%i) = %i calls = %i'%(x, Chama, SegFib(x)),end='\n')
    i = i+1
