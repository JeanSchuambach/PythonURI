Num = int(input())
Cont = 0

for Cont in range(1,Num+1):
    if Num % Cont==0:
        print(Cont, end='\n')

