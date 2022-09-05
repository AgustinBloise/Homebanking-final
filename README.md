# Homebanking Final

Homebanking completamente funcional basado en una DataBase que permitirá su registro únicamente si dicha persona ya es cliente del banco y aún no posee una cuenta de homebanking. 

El acceso le permitirá visualizar toda la información referida a sus cuentas, tarjetas, movimientos, transferencias y podrá solicitar préstamos preaprobados dependiendo de su categoría de cliente y sus límites.

Además incorpora un Script que genera un api privada, útil para interactuar con la información del homebanking, creada utilizando Django Rest Framework. Esta podra ser consultada por clientes o empleados y dependiendo de su categoría le dara accesos a diversos recursos. Sumado a esto incorpora una api pública cuyo objetivo es listar las sucursales del banco con su respectiva información.

## Dependencias

* python 3  https://www.python.org/downloads/

* Django https://www.djangoproject.com/download/

* Django Rest Framework https://www.django-rest-framework.org/

* SQLite https://www.sqlite.org/download.html

* DB Browser https://sqlitebrowser.org/dl/

## Instalacion

Para instalar en Linux

$ sudo apt-get install python3

Para instalar el resto de los requerimientos

$ pip install -r requirements.txt

## Correr el programa

* Crear ambiente virtual y activarlo:
$ python3 -m venv env
$ env/scripts/activate

* Instalar requerimientos

* Posicionarse en el directorio "homebanking":
$ cd homebanking

* Activar el servidor:
$ python3 manage.py runserver

* Acceder al servidor:
http://127.0.0.1:8000/

* Acceder a la api:
http://127.0.0.1:8000/api/

* Acceder a los prestamos de una sucursal:
http://127.0.0.1:8000/api/prestamos_por_sucursal/(id de la sucursal deseada)

* Acceder a las tarjetas de un cliente:
http://127.0.0.1:8000/api/tarjetas/(id de cliente deseado)

* Acceder al listado publico de sucursales:
http://127.0.0.1:8000/api/sucursales/
