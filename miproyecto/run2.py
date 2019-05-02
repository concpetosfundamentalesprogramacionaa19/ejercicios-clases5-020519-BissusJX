"""
  file : run.py
  autor : @BissusJX
"""

from misvariables import *

#Uso de condicional simple

nota = 18

nota = input ("Ingrese nota 1 :\n")
nota2 = input ("Ingrese nota 2 :\n")

nota = int (nota)
nota2 = int (nota2)

if nota >= 18:
   print("%s, su valor de nota es %d" % (mensaje, nota))
else:
	print ("%s - %d" % (mensaje2, nota))

if nota2 >= 18: 
   print("%s, su valor de nota es %d" % (mensaje, nota2))
else: 
   print("%s - %d" % (mensaje2, nota2)) 
