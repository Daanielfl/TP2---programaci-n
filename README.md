# Proyecto de Envío de Emails con Tkinter en Python

>Este proyecto implementa un sistema para enviar correos electrónicos utilizando Python,
>con una interfaz gráfica para facilitar la entrada de datos y la visualización de resultados.

## Funcionalidades Principales
- Envío de gmails con la direccion de SMTP.
- Interfaz gráfica para ingresar destinatarios, asunto, y contenido del mensaje.
- Validación de datos junto a una notificación de envío exitoso.

## Descripción del Proyecto y Modificaciones
El proyecto se diseñó inicialmente como una aplicación CLI simple para enviar correos. Posteriormente, se realizaron las siguientes modificaciones:
- Implementación de un Option Menu usando  `Tkinter`.
- Cambie el logo que tenía por defecto, agregue uno personalizado.
- Al emviar el mensaje de "enviado exitosamente!" para confirmar solo el éxito del correo enviado.

### GUI terminada
![](/ENVIAR_EMAIL/GUI-Personalisada.JPG)

> Agregue un combo box para que se vea mas prolijo, no guarda emails que vaya agregando el usuario, solo muestra las que estan guargadas por defecto
> lo que hice fue crear solo una lista en donde guarde correos como String y despues en el combo box muestro la lista completa
