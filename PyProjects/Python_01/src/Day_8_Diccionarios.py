# Diccionarios 
## tienen un funcionamiento parecidos a los hashmaps 
## 

first_dict = dict()
# se crean valores clave-valor
second_dict = {
            "Nombre": "Ismael"
            ,"Apellido":"Freire"
            ,"Edad":19
            ,"Lenguajes":{"Python", "C++", "Java"}
            }
print(second_dict)
print(len(second_dict)) # el len del diccionario devolvera cuantas claves estan asociadas a un valor
print(second_dict["Nombre"])
# sobrescribir con un nuevo valor
second_dict["Nombre"]="Juan"
print(second_dict["Nombre"])
# agregar nuevos valores
second_dict["Calle"] = "Ajavi"
print(second_dict)
# eliminar un valor
del second_dict["Calle"]
print(second_dict)
# validar si una clave esta en el diccionario
print("Nombre" in second_dict) # devuelve True porque la clave esta en el diccionario 
print("Ismael" in second_dict) # devuelve False porque no es una clave 

# imprimir ciertos valores
print(second_dict.items()) # items devuelve un listado con cada item 
print(second_dict.keys()) # keys devueve las claves
print(second_dict.values()) # values devuelve los valores de las claves
keys = dict.fromkeys({"Nombre", "Apellido", "Piso"}) # crea un diccionario vacio con ciertas claves
print(keys)
# forma para usar fromkeys creando un diccionario vacio con claves de otro 
third_dict = dict.fromkeys(second_dict)
print(third_dict)
# a este anterior se le puede agregar valores pero directamente a todas las claves
third_dict = dict.fromkeys(second_dict, "Brenda")
print(third_dict) # {'Nombre': 'Brenda', 'Apellido': 'Brenda', 'Edad': 'Brenda', 'Lenguajes': 'Brenda'}

# ¿y si se lo transforma a...?
print("Lista de valores",list(second_dict.values())) # crea una lista de los valores de las claves
print("Lista de claves", list(second_dict.keys())) # crea una lista de las claves
print("Tupla", tuple(second_dict)) # crear una tupla de las claves
print("Set", set(second_dict)) # crear un set de las claves