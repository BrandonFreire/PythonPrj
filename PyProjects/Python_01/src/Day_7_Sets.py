# Sets
## un sets tiene de base un array, pese a que este no existe y en PYTHON se tienen listas directamente.
first_set = set() # creacion del set() con su palabra reservada
second_set = {} # tambien se declara usando corchetes pero en un principio se crea como un diccionario, unicamente hasta que se coloque datos 
print(type(second_set)) # devuelve que es un diccionario 
# si se incertan datos 
second_set = {"Ismael", "Freire", 19} 
print(type(second_set)) # devolvera que es un set

print("----------")
# Operaciones con sets
## primero se tiene que un set no es una estructura ordenada
## los elementos de un set no se pueden repetir
## no se puede acceder a un set por sus indices 
# add
second_set.add("BrendaPower")
second_set.add("Brenda")
print(second_set)

# devuelve true or false, permitiendo que se realicen busquedas
print("BrendaPower" in second_set) 
print("Brend" in second_set)
# remove 
second_set.remove("BrendaPower")
print(second_set)
# clear: borra todos los elementos que contiene el set
#-> second_set.clear()
print(len(second_set)) # devuelve el tamaño del set luego de ejecutar un clear
# del 
del second_set # no vacia los elemenos, en realidad elimina todo el objeto 
 
print("-------------")
first_set = {"Ismael", "Freire"}
first_list = list(first_set)
print(first_list) # convierte el set en una lista pero NO es recomendable acceder a sus elementos por indices ya que no se conoce desde un principio el orden del set

print("-------------")
second_set = {"Java", "Python"}
# union
new_set = first_set.union(second_set)
print(new_set) # devuelve un nuevo set con todos los elementos de ambos sets
print(new_set.union({"MySQL", "C++"}))

# diference
print(first_set.difference(second_set)) # en first se quitan los elementos de second set
