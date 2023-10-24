Ejercicio 5
Enunciado: Debe permitirse registrar contactos, incluyendo el nombre completo, el número de documento, la dirección, número telefónico de contacto, dirección de correo electrónico.
Aclárese que debe permitirse el registro de más de un número telefónico, así como más de una dirección de correo electrónico.
Debe poderse listar los contactos con su información completa, así como permitirse la modificación y eliminación de estos

Este proyecto fue desarrollado con el framework de Django, basado en Python, cumple con todos los requerimientos solicitandos en el enunciado, la base de datos utilizada en este caso fue MySQL y la herramienta para control de versiones fue GitHub

El uso de Django implica que utiliza la arquitectura Modelo Vista Controlado (MVC), separando así el funcionamiento del modelo, sus controladores y las respuestas, además de usar buenas prácticas como lo son nombres de variables claros, código legible y entendible

Para la ejecución del proyecto es necesario tener una versión reciente de Python instalada en la máquina así como el gestor de paquetes "pip", el gestor de base de datos de MySQL, el archivo con el script de SQL está adjunto en el repositorio nombrado como script.sql

Pasos:
  1. Crear un entorno virtual de python y activarlo
  2. Instalar las dependencias de djangorestframework, django-cors-headers
  3. Ejecutar el script adjunto para la creación de la base de datos
  4. En el archivo settings.py del repositorio, ir a la variable DATABASES, en las propiedades de USER y PASSWORD utilizar las credenciales utilizadas en la máquina
  5. Correr el comando python manage.py runserver 8000 para correr el servidor, en cuanto el servidor está corriendo, se pueden hacer uso de los endpoints que se encuentran en la documentación de la API

La documentación de la API se hizo utilizando la herramienta Postman la cual se puede encontrar en el siguente link 
https://documenter.getpostman.com/view/27902729/2s9YRDypwV
