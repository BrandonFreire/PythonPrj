# DICCIONARIOS : tablas hash en python
d_1 = {"nombre":"Juan", "edad":28, "semestres":[1,2,3]}
d_2 = {1:100, 2: True, 3:"Hola", 4 : 5.8}

# bucle for que imprimirá todas las claves en el diccionario
for item in d_1:
    print(item)

print(d_1.items())

print(type(d_1["edad"]))

print(d_2[4])

print(d_1)

# iteracion sobre items()
for i in d_1.items():
    print(i) # imprime la clave y el valor

for key, value in d_1.items():
    print(f"La clave es {key} y el valor es {value}") # imprime la clave y el valor

# no se puede imprimir:
## print(d_1.items()[0])
# pero si se puede imprimir
print(list(d_1.items())[0])

print("-----------------")

d_3 = {1:"hola", 2: "Fernando", 3:d_1}
print(d_3[3]["nombre"])

print(d_3)

# funcion get:  trabaja unicamente con claves
print("---------------------")

print(d_2.get(1, "no existe")) #->devolvera el valor de 1
# sino existe devolvera
print(d_2.get(5,"no existe"))

print("-----------")

def calcular_x (numeros):
    for item in numeros:
        if item%2==0:
            print(item, end=" ")


calcular_x([1,2,3,4,5,7,8,9])