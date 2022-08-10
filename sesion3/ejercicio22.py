
'''
*********** Programacion Acelerada
File: sesion3/ejercicio21.py
Autor: Programador jackie
Action: numero de mayor a menor
'''

loteria = []
n=1
while n==1:
  numero= int(input("numero ganador"))
  loteria.append(numero) 
  n= int(input("Desea agregar otro? 1=si 2=no"))  
orden = sorted(loteria)  
print("Lista ordenada de menor a mayor", orden)
for j in loteria:
  print("lista desordenada ", j)  
