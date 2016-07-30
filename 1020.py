# -*- coding: utf-8 -*-

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


'''
d = int(input())

a = int(d / 365)
aux = d % 365
m = int(aux / 30)
d =  aux % 30

print("%i ano(s)" %a,end='\n')
print("%i mes(es)" %(m),end='\n')
print("%i dia(s)" %d,end='\n')
'''