# Tupla
## definicion 
first_tupla = tuple() # definicion por el nombre reservado 
second_tupla = () # definicion por los parentesis
## una tupla es un conjunto de valores, no es igual a una lista, sino se trabaja con valores inmutables. Es decir, los valores no se pueden superponer sobre los definidos, se vuelven constantes.
## ademas, se tiene que los elementos se insertan ordenadamente y permite repetidos
first_tupla = (35, 1.66, "Ismael", "Freire")
print(first_tupla)

second_tupla = (40,125,7,89,12,56)
print(second_tupla)

print(first_tupla+second_tupla)

sum_tuple = first_tupla+second_tupla
print(sum_tuple)
print(sum_tuple[1:4]) #sublista, entre el rango propuesto entre i hasta i-1

# count(): cuenta las ocurrencias 
# index(): devuelve el indice de cierto valor
print(first_tupla.index(1.66))
# insert()
## se transforma a una lista
first_tupla = list(first_tupla)
print(type(first_tupla))

first_tupla[3] = "BrendaPower"
first_tupla.insert(0,"Mestizo")
first_tupla = tuple(first_tupla)
print(first_tupla)

# del: no es tipico de las tuplas, entonces elimina la variable porque lass tuplas son inmutables  
del first_tupla
# print(first_tupla) -> y la vuelve no definida, retorna un error