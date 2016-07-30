cont = 1
impar = 0
pares = 0
Pos = 0
Neg = 0

while(cont<=5):
    x = int(input())
    if x%2==0:
        pares = pares + 1
    else:
        impar = impar + 1
    if x > 0:
       Pos = Pos + 1
    else:
        Neg = Neg + 1
    cont = cont + 1


print("%i valor(es) par(es)" %pares, end='\n')
print("%i valor(es) impar(es)" %impar, end='\n')
print("%i valor(es) positivo(s)" %Pos, end='\n')
print("%i valor(es) negativo(s)" %(Neg-1), end='\n')