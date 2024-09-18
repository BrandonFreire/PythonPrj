# Bucles
## While
print("---------WHILE---------")
condition = 0
while condition<10:
    print(condition)
    # si la condicion cambia, se terminara la ejecucion en un punto 
    condition += 2
else:
    print("La condicion es mayor o igual que 10")

print("------------------")
while condition < 20:
    condition += 2
    if condition == 16:
        print("La condicion es igual a 16")
        break
    print(condition)

print("---------FOR---------")
## For
frutas_list = ["manzana", "pera", "naranja", "uvas"]
for elementos in frutas_list:
    print(elementos)
print("----------")

first_tupla = (35, 1.66, "Ismael", "Freire")
for elementos in first_tupla:
    print(elementos)
print("----------")

second_dict = {
            "Nombre": "Ismael"
            ,"Apellido":"Freire"
            ,"Edad":19
            ,"Lenguajes":{"Python", "C++", "Java"}
            }
for elementos in second_dict.values():
    print(elementos)
    if elementos == 19:
        # break: para terminar la ejecucion del programa
        continue # detiene la ejecucion en un punto del programa y vuelve al incio del for
else:
    print("No hay mas elementos en el diccionario")

print("----------")

# for elementos in second_dict:
#     for values in second_dict.values():
#         print(elementos, values)

# Ejercicios
print("1- Triangulo invertido")
# # filas = int(input("Ingrese el tamaño del triangulo "))
# # for i in range(1, filas+1, 1):
# #     print(i * "*")

print("2- Crear un cuadrado")
# # lado = int(input("Ingrese el tamaño del cuadrado: "))
# # for fil in range(lado):
# #     for col in range(lado):
# #         print("* ", end="")
# #     print()

print("3- Crear un cuadrado vacio")
# # lado = int(input("Ingrese el tamaño del cuadrado: "))
# # for i in range(lado):
# #     if i == 0 or i == lado-1:
# #         print("*"*lado)
# #     else:
# #         print("*" + " "*(lado-2) + "*")

print("3- Imprimir las tablas de multiplicar")
# # contador=0
# # for i in range(0,11,1):
# #     print("{} * {} = {}".format(contador, i, contador*i))
# #     contador += 1

print("4- iterar del 0 al 100 e imprimir la suma de todos los numeros")
suma = 0
for i in range(0,101,1):
    suma += i
print(suma)
