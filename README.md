# Hostal

este proyecto es una aplicación web responsiva desarrollada con el framework de Python "Django" una base de datos "No SQL" (SQLITE), cuyo uso es para la realización de reservas en una hostal, también cuenta con un panel de administración para gestionar todo el negocio.

pasos para inicializar :

* tener instalado python en su equipo antes de la utilizacion de este programa *

1) se debe cambiar la ruta del proyecto desde la carpeta env" encontrarán un archivo llamado "pyvenv.cfg".

2) dentro de este archivo verán lo siguiente : home = C:\Users\NombreEquipo\AppData\Local\Programs\Python\Python39

3) donde dice "NombreEquipo" coloque el nombre de ruta de su equipo utilizado y la carpeta "Python39" debe ser correspondiente la version de python instalada en su pc,
en este caso yo utilize la version 3.9 


- ahora vamos a iniciar la app, primero iniciaremos el servidor local.

ya estando en la raiz del proyecto, en la consola ejecute los siguientes comandos :

1. cd env 
2. cd scripts
3. ./activate (esto activará el servidor local)
4. cd.. (x2 , para volver a la carpeta raiz)
5. cd hotal
6. py manage.py runserver

y listo se deberia activar su servidor local y podrá hacer el uso de este programa.

PD: en caso de tener problemas en la inicializacion del servidor, desinstale los pip y vuelva a instalarlos.
ingresando en la consola:

1. pip uninstall pip
2  (preguntará si quieres borrar los pip) "si a todo".
3. pip install pip

ahora inicia el servidor nuevamente.
