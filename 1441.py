'''
Fazer sequencia granizo
se par - (1/2)Hn-1
se impar - 3Hn+1
O programa deve gerar a sequencia porém só mostrará o melhor valor
programa para de rodar quando 0 for digitado
'''
#subprogramas
def Granito(num):
    global maiorNum
    maiorNum = 0
    while num!=1:
        if num%2==0:
            num = num/2
            DecMaior(num)
        else:
            num = 3*num+1
            DecMaior(num)
    return maiorNum
    
def DecMaior(num):
    global maiorNum
    if num > maiorNum:
        maiorNum = num


#programa Principal
maiorNum = 0
num = int(input())

while (num!=0):
    print(Granito(num))
    num = int(input())
    