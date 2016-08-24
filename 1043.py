'''
Leia 3 valores reais (𝐴, 𝐵 e 𝐶) e verifique se eles formam ou não um triângulo. Em caso positiv
o, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem 𝐴 e 𝐵 como base e 𝐶 como altura, mostrando a mensagem
Area = XX.X
Entrada
A entrada contém três valores reais, na mesma linha.
Saída
O resultado deve ser apresentado com uma casa decimal.
Exemplo
Entrada
Saída
6.0 4.0 2.0
Area = 10.0
Entrada
Saída
6.0 4.0 2.1
Perimetro = 12.1
'''
vet = input().split()
a = float(vet[0])
b = float(vet[1])
c = float(vet[2])

#impressao
if a >= b+c:
    # calcular o trapezio
    area = ((a+b)*c)/2
    print("Area = %.1f" %area, end='\n')
else:
    triangulo = a+b+c
    print("Perimetro = %1.1f" %triangulo, end='\n')   