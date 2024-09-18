# Condicionales
first_condition = False

if first_condition :  # lo anterior es igual a escribir first_condition == True
    print("La condición es verdadera")  # La condición es verdadera

first_condition = 5*5
if first_condition > 10 and first_condition < 20 :
    print("La condición es verdadera")  # La condición es verdadera
elif first_condition == 25 :
    print ("Es igual a 25")
else:
    print("La condición es falsa")  # La condición es falsa

# print("La ejecucion continua")

print("--------------------")
first_string = ""
if not first_condition:
    print("La condición es falsa y la cadena es vacia")  # La condición es falsa
else:
    print("La condición es verdadera y la cadena no es vacia")  



print("--------------")
# Ejercicio 1: 
# 1. Pedir al usuario que ingrese su edad
edad = int(input("Cual es tu edad "))
#edad = int(edad)

if edad > 0 and edad <= 10:
    print("Eres un niño")
elif edad >= 11 and edad <20:
    print("Eres un adolescente")
elif edad >=20 and edad <80:
    print("Eres un adulto")
else:
    print("No existe esa edad")