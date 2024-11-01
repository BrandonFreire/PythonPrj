# Funciones 

def function (n):
    print("Esto es una funcion")
    for i in range (n,n+10,2):
        print(i, end=" ")

#print("Hola ingresa los numeros a imprimir")
#function(int(input()))
#function()

def sum_values (first, second):
    print(first, second)

# value_1 = int(input())
# value_2 = int(input())
# sum_values (value_1, value_2)

def sum_values_return (valor_1, valor_2):
    if valor_1 > valor_2:
        return valor_1
    else:
        return valor_2
    
# if sum_values_return (2,1) > 2:
#     print("El valor mayor es 2")
# else:
#     print("el valor no es mayor a dos")

def name (name, lastname):
    print("Hola mi nombre es {} y mi apellido es {}".format(name, lastname))

# name(lastname="Freire", name="Ismael")

# parametros por defecto: se define valores por defecto por si no se ingresan valores 
def par_default (name, lastname, alias="Sin alias"):
    print("Hola, mi nombre es {} {} y mi alias es {}".format(name, lastname, alias))

# par_default("Ismael", "Freire", "Brenda")

# Infinitos parametros: se antecede con el signo "*" a la variable
def par_infinitos (*texts):
    for text in texts:
        print(text.upper())

par_infinitos("Hola", "Bine")