# Comandos

*ls*    -> se tiene acceso a los ficheros
*cd + tab*    -> permite movilizarse por los ficheros
*cd ..*    -> permite regresar al directorio anterior
*cd ~*    -> permite regresar a la carpeta raiz
pwd         -> devuelve cual es el lugar donde nos encontramos en el equipo
mkdir + "name" -> crea una carpeta en el fichero donde nos encontremos
git confif --global -> indica que se va a trabajar de forma global, es decir afectara a todo git desde mi maquina
git config --global user.name "nombre" -> indica que el nombre del usuario es "nombre"

touch name.py -> crea un fichero de codigo en algun lenguaje en particular
git init      -> hace que un directorio empiece a funcionar git, es decir, se ha creado un control de versiones (un repositorio de git)
git status    -> arroja el estado del repositorio

## Guardar una fotografia del fichero

1. Primera fotografia del fichero   -> *git add name.py*
mientras que para añadir todos los ficheros pendientes se usa-> *git add .*
2. Segunda fotografia del fichero   -> *git commit -m "mensaje"*
3. Tercera fotografia del fichero   -> *git log*
este ultimo muestra el commit

## No realizar los cambios

*git checkout  name.py*      -> se situa en un punto en concreto de una fotografia

## Otras formas de ver las ramas y commit

*git log --graph*            -> muestra de forma grafica la rama
*git log --graph --pretty=oneline*            -> muestra de forma grafica la rama
*git log graph --decorate --all --oneline*    -> muestra en una linea los commits realizados

## Creaccion de alias

1. *git config --global alias.NAME "INSTRUCCION"*
ej:
git config --global alias.commitLine "log --graph --decorate --all --oneline"
siendo *git commitLine* el nuevo alias para mostrar en una linea loss commits realizados

## GitIgnore

*touch .gitignore* -> se crea en la raiz del proyecto
se suele usar *touch* pero sino funciona, se debe usar *echo*
si tampoco funciona se debe usar *New-Item .gitignore -ItemType File*

- para agregar un archivo a gitignore unicamente se debe ingresar su nombre con el .tipoDeArchivo

## Buscar los cambios que se han hecho

*git diff*       -> muestra los cambios exactos que se han hecho, esto permite ver que se ha cambiado sin haber realizado una fotografia

## Otras formas de moverse

*git checkout HEAD* -> indica donde es la nueva cabeza del proyecto

## Descartar cambios

*git reset --hard +ID_del_commit*            -> se posiciona en un ID de alguno de los commits realizados, pero "elimina" los posteriores a este. Si se quiere recuperar lo que se "elimino" mediante **git reflog** se puede conocer el ID del ultimo commit realizado y con **git reset** mas el ID se puede regresar al ultimo commit

- para ver todos los movimientos -> *git reflog*

## TAG

Son puntos importantes donde en alguno de estos se desea guardar la informacion. Siendo las versiones en las aplicaciones, por ejemplo hasta cierto commit se usan todos los anteriores para crear alguna version

*git tag NAME*              -> crea la primera version

*git tag*                   -> muestra todos los tag creados
*git checkout tags/name*    -> se posiciona en un tag
*git checkout main*         -> se vuelve al punto de inicio
