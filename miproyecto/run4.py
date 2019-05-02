"""
   deseamos optener el costo de una carrera universitaria.
   El valor promedio de cada ciclo es de 1200$, el valor promedio del seguro educativo por ciclo es de 100$
   si la edad del estudiante es menor o igual a 20 caso contrario sera de 150$ si el estudiante 
   tiene una modalidad a distancia el numero de ciclos a seguir es de 10 caso contrario debera seguir 8 ciclos 
   obtener la proyeccion del costo de la carrera de un estudiante.
"""
valorPromedio = 1200

edad = input("ingrese la edad del estudiante\n")
modalidad = input ("ingrese la modalidad del estudiante si es a distancia ingrese 1 y si es Presencial ingrese 2 \n")
#ciclo = input ("ingrese el ciclo en que se encuentra el estudiante\n")
edad = int (edad)
modalidad = int (modalidad)
seguro = 0
seguro = int (seguro) 
if (edad <= 20) and (modalidad == 1):
     seguro = 10 * 100
     
else:
   	if (edad > 20) and (modalidad == 1):
   	     seguro = 10 *150
           
if (edad <= 20) and (modalidad == 2):
     seguro = 8 * 100
     
else:
      if (edad > 20) and (modalidad == 2):
           seguro = 8 *150
   	    
if (modalidad == 1):
   total = (valorPromedio * 10)
else:
   total = (valorPromedio * 8) 

total = total + seguro
print (total)

