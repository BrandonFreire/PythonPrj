# Clases
'''
se pueden llamar a clases sin parentesis o con parentesis, a menos que se necesite pasarle parametros 
''' 
class EmpyPerson:
    pass
    # la instruccion pass: Cuando se ejecuta la instrucción pass, no sucede nada, pero se evita obtener un error cuando NO se permite código vacío

class Person ():
    def __init__(self, name="vacio", age="vacio"):
        # la palabra reservada de init es un método especial que se llama cada vez que se instancia una clase y sirve para inicializar el objeto que se crea, es un constructor de clase.
        self.name = name # "Ismael"
        self.age= age    # "20"

# person = Person("Ismael", "20")
# print("Hola mi nombre es {} y mi edad es {}".format(person.name,person.age))

class Person_2 ():
    def __init__(self, name="vacio", lastname="vacio", alias="vacio"):
        self.full_name = "{} {} ({})".format(name, lastname, alias)
        self.__alias = alias # colocar a un atributo como privado

    # getter y setter
    def get_alias (self):
        return self.__alias
    
    def set_alias (self, alias):
        self.__alias = alias
    
    # metodos
    def walk (self):
        print("{} esta caminando".format(self.full_name))

person_2 = Person_2("Alejandro", "Mor")
print(person_2)
person_2.walk()

person_2.full_name = "Hector Marlon (Loco)"
print(person_2.full_name)

person_2.set_alias("Bueno")
print(person_2.get_alias())
