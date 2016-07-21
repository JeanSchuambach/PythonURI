Vet1=input().split()

a = int(Vet1[0])
b = int(Vet1[1])
c = int(Vet1[2])

Maior = (a+b+abs(a-b))/2
Final = (Maior+c+abs(Maior-c))/2

print("%i eh o maior" %Final, end='\n')