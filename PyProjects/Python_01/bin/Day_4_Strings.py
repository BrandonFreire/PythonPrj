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