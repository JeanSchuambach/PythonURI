X = int(input())
In = 0
Out = 0
cont = 0

while (cont < X):
    A = int(input())
    if 10<=A<=20:
        In = In + 1
    else:
        Out = Out + 1
    cont = cont + 1

print("%i in" %In, end='\n')
print("%i out" %Out, end='\n')