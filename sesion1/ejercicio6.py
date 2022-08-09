'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio6.py
Autor: Programador JACKIE
Action: imprime capital obtenido de una inversión
'''
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str((cantidad * (interes / 100 + 1) ** años, 2))) 