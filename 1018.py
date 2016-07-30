X = int(input())

print(X, end='\n')
for i in [100, 50, 20, 10, 5, 2, 1]:
    print("%i nota(s) de R$ %1.2f" %((X / i),i), end='\n')
    print(X-(X/i)*i)
