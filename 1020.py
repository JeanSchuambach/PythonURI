Tempo = int(input())

Anos=0
Meses=0
Dias=0

if Tempo>365:
    Anos = int(Tempo/365)
    Tempo = Tempo % 365
    Meses = int(Tempo/30)
    Dias = Tempo % 30
else:
    Meses = int(Tempo/30)
    Dias = Tempo % 30


    
print("%i ano(s)\n%i mes(es)\n%i dia(s)" %(Anos, Meses, Dias), end='\n')