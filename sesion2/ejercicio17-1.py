'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio17.py
Autor: jackie
Action: permite ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo.
Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36
'''
valor = int(input("Ingrese valor:"))
print("tabla de multiplicar del ", valor)
if valor !=3 and valor >0 and valor < 11:
  
     for t in range(11):
        r = t * valor
        print(r)
if valor == 3:
  for i in range(1,13):
      r = i * valor
      print(r)