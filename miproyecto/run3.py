"""
  file : run.py
  autor : @BissusJX

  nota mayor o igual a 18 sobresaliente 
....
  nota mayor o igual a 16 y menor a 18:muy buena

  nota mayor o igual a 13 y menor a 16: buena
....
  nota menor a 13: insuficiente 
""" 

#from misvariables import *

#Uso de condicional simple


nota = input ("Ingrese nota 1 :\n")

nota = int (nota)

if nota >= 18:
   print("%s- nota %d" % ("sobresaliente", nota))
else:
	if (nota >= 16) and (nota <18):
		print("%s - nota %d" % ("Muy buena", nota))
	else:
		if (nota >= 16) and (nota < 16):
			print ("%s - nota %d" % ("Buena", nota))
		else:
			print ("%s - nota %d" % ("Insuficiente", nota))

