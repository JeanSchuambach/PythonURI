X = int(input())

print(X, end='\n')
for I in [100, 50, 20, 10, 5, 2, 1]:
    J = int(X/I)
    print("%i nota(s) de R$ %i,00" %(J,I), end='\n')
    X = X - J*I