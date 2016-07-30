X = int(input())
Y = int(input())
Soma = 0

if X > Y:
    for i in range(Y+1, X):
        if not (i%2==0):
            Soma = i + Soma
else:
    for a in range(X+1, Y):
        if not (a % 2 == 0):
            Soma = a + Soma

print(Soma, end='\n')