pares = 0
impares = 0
i = 0
pos = 0
neg = 0

#codigo
while i != 5:
    a = int(input())
    if a % 2 == 0:
        pares = pares+1
    else:
        impares = impares+1
    if a > 0:
        pos = pos+1
    else:
        neg = neg+1
    i = i+1
        
print('%i valor(es) par(es)\n%i valor(es) impar(es)\n%i valor(es) positivo(s)\n%i valor(es) negativo(s)'%(pares, impares, pos ,neg), end='\n')