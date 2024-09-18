# Variables...
"""
se nombre variables en minusculas 
se declaran variables con cualquier nombre pero asignando el tipo de dato
"""

variable_str = "mi variable string"
variable_int = 2
variable_bool = True
print(type(variable_str))
print(type(variable_int))
print(type(variable_bool))

print(variable_str, variable_int, variable_bool) #concatenar
print(str(variable_int)) #transformar variable de tipo int a string
print(str(variable_int) +" "+ variable_str) #concatenar string con int transformado a string

## concatenar de diferentes formas
print("El numero es ", variable_int)
print("El valor booleano es ", variable_bool)

## variables en una sola linea
variable_name, variable_lastname, variable_age = "Ismael", "Freire", 19
print(f"El nombre es {variable_name} su apellido es {variable_lastname} y su edad es {variable_age}")
print("El nombre es ",variable_name,variable_lastname," y su edad es ",variable_age)

##Funciones del sistema 
print(len(variable_str)) # len() retorna el numero de items incluidos los espacios 
variable_name = input("Hola, cual es tu nombre ") # input()
print (variable_name)

## Asignar un valor a una variable ya como un tipo de dato definido, es decir forzar el tipado "tipar"
## es decir, el tipado de Python es dinamico
variable : str = "string" # se tipa para saber que se tiene un string 
variable = 32 # con lo que luego sigue siendo posible transformarlo a otro tipo de dato
print(type(variable))