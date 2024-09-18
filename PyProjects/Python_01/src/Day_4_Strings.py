# Strings

var_str = "string"
var_other_str = 'string'

print(var_str + var_other_str)

var_str_sal = "String en una linea \n con salto de linea" 
print (var_str_sal)

var_str_tab = "\tStribg con tabulacion"
print(var_str_tab)

var_str_tab_sal = "\tString tabulado \nString escapdo"
print(var_str_tab_sal)

var_str_ignore = "\\t String que ignora tab \\n String que ignora salto de linea"
print(var_str_ignore)

#Formateo
# se formatea un string con %s
# se formatea un entero con %d
# se formatea un float con %f
name, last_name, age = "Ismael", "Freire", 20
print("Hola soy %s %s y tengo %d años" % (name, last_name, age))

print("Hola soy {} {} y tengo {} años".format(name, last_name, age))

print(f"Hola soy {name} {last_name} y tengo {age} años")

# Desempaquetado de caracteres

language ="Python"

a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division 
print("---------------")
language_slice = language[1:4]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] # el "2" señala los saltos
print(language_slice)

# Reverse
print("---------------")
reversed = language[::-1]
print(reversed)

# Funciones
print("-------------")
print("Funciones")
language_1 = "python"
print(language_1.capitalize()) # primera en mayusculas
print(language_1.upper()) # todas en mayusculas 
print(language_1.count("t")) # cuenta la frecuencia de la letra "t"
print(language_1.isnumeric()) # ve si es numerico, devuelve true or false
print(language_1.isalpha()) # ve si es alfanumerico, devuelve true or false
print(language_1.lower()) # todas minusculas
print(language_1.isupper()) # valida si esta todo en mayusculas, devuelve true or false
print(language_1.upper().islower()) # concatena, se ejecuta de izquierda a derecha y devuelve true or false por "islower()"
print(language_1.startswith("py")) # valida si algo empieza con cierto caracter, devuelve true or false, es sensible a las mayusculas
print(language_1.endswith("n")) # valida si algo termina con cierto caracter, devuelve