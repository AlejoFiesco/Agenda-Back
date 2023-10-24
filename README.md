Ejercicio 5

Enunciado: Debe permitirse registrar contactos, incluyendo el nombre completo, el número de documento, la dirección, número telefónico de contacto, dirección de correo electrónico.
Aclárese que debe permitirse el registro de más de un número telefónico, así como más de una dirección de correo electrónico.
Debe poderse listar los contactos con su información completa, así como permitirse la modificación y eliminación de estos

Este proyecto fue desarrollado con el framework de Django, basado en Python, cumple con todos los requerimientos solicitandos en el enunciado, la base de datos utilizada en este caso fue MySQL y la herramienta para control de versiones fue GitHub

El uso de Django implica que utiliza la arquitectura Modelo Vista Controlado (MVC), separando así el funcionamiento del modelo, sus controladores y las respuestas, además de usar buenas prácticas como lo son nombres de variables claros, código legible y entendible; así mismo se hace un modelo de datos sencillo y normalizado con el que es fácil trabajar

Adicional, se utilizan encabezados CORS para una mayor seguridad, permitiendo únicamente peticiones desde la dirección http://localhost:3000 que es donde se aloja el cliente

Para la ejecución del proyecto es necesario tener una versión reciente de Python instalada en la máquina así como el gestor de paquetes "pip", el gestor de base de datos de MySQL, el archivo con el script de SQL está adjunto en el repositorio nombrado como script.sql

Pasos:
  1. Crear un entorno virtual de python y activarlo
  2. Instalar las dependencias de djangorestframework, django-cors-headers
  3. Ejecutar el script adjunto en MySQL Workbench para la creación de la base de datos
  4. En el archivo settings.py del repositorio, ir a la variable DATABASES, en las propiedades de USER y PASSWORD utilizar las credenciales utilizadas en la máquina
  5. Correr el comando python manage.py runserver 8000 para correr el servidor, en cuanto el servidor está corriendo, se pueden hacer uso de los endpoints que se encuentran en la documentación de la API

La documentación de la API se hizo utilizando la herramienta Postman la cual se puede encontrar en el siguente link 
https://documenter.getpostman.com/view/27902729/2s9YRDypwV

Esta documentación fue hecha con ejemplos reales de la aplicación corriendo, ejemplos que Postman automáticamente agrega a la documentación 

El servidor ejecuta las siguientes acciones, se mostrará capturas de pantalla de la ejecución en Postman incluyendo los datos necesarios para el correcto funcionamiento, como los datos de salida del endpoint

  1. Agregar un nuevo contacto:
     
     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/60488a35-eae2-4145-94f6-881a6f749ca8)
     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/48af2c69-0318-4b5d-9ec4-468b6212346e)

  2. Obtener listado de contactos

     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/13426dde-d47f-419d-9bbf-4b1b9a654656)
     Debido a que no se ve en su totalidad los resultados en la captura, se copia la respuesta del servidor a esta misma petición
     {
    "personas": [
        {
            "numero_documento": 78945632,
            "telefonos": [
                {
                    "id": 8,
                    "telefono": 3016666666,
                    "persona": 78945632
                }
            ],
            "emails": [
                {
                    "id": 9,
                    "email": "correo3@example.com",
                    "persona": 78945632
                }
            ],
            "nombre_completo": "Maria Diaz",
            "direccion": "Tunal"
        },
        {
            "numero_documento": 123456788,
            "telefonos": [
                {
                    "id": 5,
                    "telefono": 3211234567,
                    "persona": 123456788
                }
            ],
            "emails": [
                {
                    "id": 6,
                    "email": "correo@example.com",
                    "persona": 123456788
                }
            ],
            "nombre_completo": "Fulanito",
            "direccion": "Calle 100"
        }
    ]
}

  3. Obtener un contacto específico

     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/95dce716-9705-4765-ab3a-f96ce25e4c97)

  4. Eliminar un contacto
     
     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/d5efbfdf-cac9-4e11-ac23-fb976c857704)

  6. Editar un contacto
     
     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/0ac0449b-9118-4355-8321-bfa54f4a44ed)
     Aquí vemos el estado anterior del registro

     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/3c410a0d-6c52-42fd-b53b-125ad7604b55)
     Y aquí vemos como se han efectuado los cambios

  8. Agregar un teléfono
     
     ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/83db085c-ad94-468c-865b-86dfe8ff7032)

  9. Editar un teléfono

      ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/0b7a7386-538b-4b59-9610-e6c49b549887)

  10. Eliminar un teléfono

      ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/4b1f0d9a-8c38-4ca3-b764-2160ceeb723b)

  11. Agregar un nuevo email

      ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/f835d905-52ed-41c9-bca7-370d94b0470a)

  12. Editar un email

      ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/d31609d7-27dc-4f6d-bfb6-8bcf10f64b4d)

  13. Eliminar un email

      ![image](https://github.com/AlejoFiesco/Agenda-Back/assets/61293194/ef74c3ec-2fc9-4e23-ab88-466acb1c58b7)


    







