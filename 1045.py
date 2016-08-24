vet = input().split()
vet.sort()
a = float(vet[0])
b = float(vet[1])
c = float(vet[2])

#impressao
if a >= b+c:
    print('NAO FORMA TRIANGULO', end='\n')
else:
    aa = a**2
    bb = b**2
    cc = c**2
    if aa==(bb+cc):
        print('TRIANGULO RETANGULO',end='\n')
    elif aa>(bb+cc):
        print('TRIANGULO OBTUSANGULO',end='\n')
    elif aa<(bb+cc):
        print('TRIANGULO OCUTANGULO',end='\n')
if a==b==c:
    print('TRIANGULO EQUILATERO',end='\n')
else:
    if (a==b) or (a==c) or (c==b):
        print('TRIANGULO ISOSCELES',end='\n')