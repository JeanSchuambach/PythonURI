Tempo = int(input())

Min = int(Tempo/60)
Seg = Tempo % 60
Horas = 0
if Min>60:
    Horas = int(Min/60)
    Min = Min % 60

print("%i:%i:%i" %(Horas,Min,Seg), end='\n')