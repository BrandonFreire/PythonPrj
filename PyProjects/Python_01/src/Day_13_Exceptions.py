# Excepciones

## Manejo de errores

value_1 = 5
value_2 = 0

try:
    # Código que puede generar un error
    x = value_1 / value_2
except ZeroDivisionError: # ERRORES/Excepciones por tipo
    # Manejo del error
    print("No se puede dividir por cero")
else:
    # Código que se ejecuta si no se genera un error
    print("La operación se realizó correctamente")
finally: 
    # Código que se ejecuta siempre, independientemente de si se generó un error
    print("El programa ha terminado")

# Se puede colocar varios except especificando el tipo de error en cada uno 
# pero tambien se puede tener excepciones sin colocar el tipo de error 
try:
    # Código que puede generar un error
    x = value_1 / value_2
except ZeroDivisionError: # ERRORES/Excepciones por tipo
    # Manejo del error
    print("No se puede dividir por cero")

# exceptiones en los que se captura el error 
try:
    # Código que puede generar un error
    x = value_1 / value_2
except ZeroDivisionError as e:
# Una forma de controlar el error sino llegase a conocerse su tipo. Es decir, si llegase a darse otro error del cual no se tiene idea que puede pasar, es posible colocar "except Eception:"" o "except Exception as e:""
    print("Se ha producido un error de tipo->", e)