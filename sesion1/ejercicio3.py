'''

*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Programador JACKIE
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))

coste = float(input("Introduce lo que cobras por hora: "))
he = int(input("Introduce cantidad de horas extras:"))
paga = (horas * coste) + (coste * he)
print("Tu paga es", paga)
