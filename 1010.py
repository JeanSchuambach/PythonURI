vetor1 = input().split()
vetor2 = input().split()

cod1, qtde1, valor1 = vetor1
cod2, qtde2, valor2 = vetor2

TOTAL = (int(qtde1)*float(valor1)) + (int(qtde2)*float(valor2))

print("VALOR A PAGAR: R$ %1.2f" %TOTAL, end='\n')

