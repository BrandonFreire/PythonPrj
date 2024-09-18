# Listas-Arreglo-Array
## Estructura de datos ordenados y en los que puede haber repetidos
one_list = list() # definicion y creacion de una lista
print(one_list) # imprimira una lista vacia
print(len(one_list)) # imprimira el tamaño de la lista
one_list = [35,35,34,85,47]
print(one_list) # imprimira la lista con los valores
print(len(one_list)) 

print("\n----------------------")

two_list = [19, 1.66, "Ismael", "Freire"] # no hace falta guardar en la lista el mismo tipo de dato
print(two_list)
print(type(two_list))

print(two_list[1]) # acceder a una posicion en la lista
print(two_list[-1]) # se accede a un elemento empezando por el extremo derecho de la lista
print(two_list[-2]) 
print(two_list[-3])
# asi mismo se tienen errores al intentar acceder a indices fuera del tamaño de la lista:
## print(two_list[-5])
print(one_list.count(35))

print("\n----------------------")
age, height, name, lastname = two_list # desempaquetado; se debe desmpaquetar la misma cantidad de elementos en la misma cantidad de variables
print(age)

print("\n----------------------")
print(one_list + two_list) # concatenacion de listas

print("\n----------------------")
# ejemplo de tipado debil 
one_list = "tipado dinamico"
print(one_list)

print("\n----------------------")
# Operaciones
# 1. indexado: añadir un elemento al final de la lista
two_list.append("EPN")
print(two_list)

# 2. insert: se inserta un elemento en una posicion deseada
two_list.insert(0,"Mestizo")
print(two_list)

two_list[0] = "Blanco"
print(two_list)

# 3. remove: eliminar un elemento, se puede eliminar con un indice o especificando el elemento, si el elemento se repite entonces solo se borra una vez
two_list.remove("EPN")
print(two_list)

# 4. pop: elimina el ultimo elemento por defecto pero lo devuelve 
print(two_list.pop())
print(two_list.pop(0)) # se le pasa el indice
print(two_list)

# 5. delete: elimina por indice 
del two_list[2]
print(two_list)

# 6. copy: permita copiar la referencia
two_list_copy = two_list.copy()
two_list.clear()  # clear borra toda la lista
print(two_list_copy)
print(two_list)

# 7. reverse: da la vuelta a la lista
two_list_copy.reverse()
print(two_list_copy)

# 8. sort: ordena la lista
list_num = [4,2,7,10,67,10,0,63,9]
list_num.sort()
print(list_num)

print("\n----------------------")
# Creacion de sublistas
print(list_num[1:4])