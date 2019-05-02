"""
   deseamos optener el costo de una carrera universitaria.
   El valor promedio de cada ciclo es de 1200$, el valor promedio del seguro educativo por ciclo es de 100$
   si la edad del estudiante es menor o igual a 20 caso contrario sera de 150$ si el estudiante 
   tiene una modalidad a distancia el numero de ciclos a seguir es de 10 caso contrario debera seguir 8 ciclos 
   obtener la proyeccion del costo de la carrera de un estudiante.
"""
valorPromedio = 1200

edad = input("ingrese la edad del estudiante\n")
modalidad = input ("ingrese la modalidad del estudiante si es a distancia ingrese 1 sino ingrese 2 \n")
#ciclo = input ("ingrese el ciclo en que se encuentra el estudiante\n")
edad = int (edad)
modalidad = int (modalidad)
if (edad <= 20):
     seguro = 100
     
else:
   	if (edad > 20):
   	     seguro = 150
   	    
if (modalidad == 1):
   ciclo == 10
else:
   	ciclo == 8 
total = (ciclo + 1200 ) * (ciclo * seguro)
print (total)

