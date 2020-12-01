# Post
El método **POST** es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para algún recurso determinado.

## Primer Post 
En el primer post utilizaremos la [API TRELLO](https://developer.atlassian.com/cloud/trello/). Lo que estamos haciendo es crear una lista en un tablero trello.

 1. Primero tendremos que obtener el id de la tabla que se ubica en la url de la tabla *https://trello.com/b/**KF4hyh3s**/pepe*.
![enter image description here](https://i.imgur.com/7BcCTt8.png)

 2. Le hacemos  la petición a esta url *https://api.trello.com/1/boards/KF4hyh3s/lists*. 
![enter image description here](https://i.imgur.com/pXPASgu.png)

##### **PARAMETRO DE ENTRADA**
 - key: **String** *Es la clave de seguridad para autenticar el usuario. Aqui es donde se consigue [link](https://trello.com/app-key)*
 - token: **String** *Es el token de seguridad para autenticar el usuario. Aqui es donde se consigue [link](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=6e1e48f5edf778c578dcf3d9a64739fc)*
 - name: **String** *Es el nombre de la lista quu añadiremos.*

##### **PARAMETRO DE SALIDA**
- id: **String** *Id de la lista.*
- name: **String** *Nombre de la lista.*
- closed: **Boolean** *True si la lista esta cerrada o False si no esta cerrada.*
- pos: **Double** *Posición de la lista.*
- idBoard: **String** *Id de la tabla donde se crea la lista.*
- limits: **Array** *Limite de elementos que se puede añadir a la lista.*


3. Como resultado final se agrego la lista de forma correcta.![enter image description here](https://i.imgur.com/Az3QWCl.png)


# Delete
**Delete** es una sentencia de postman que permite eliminar elementos y recursos tanto del backend, base de datos, etc.

Realizaremos las peticioness **DELETE** en **GITTER** utilizando su  [api rest](https://developer.gitter.im/docs/rest-api).

## Primer delete


1. Primeramente **crearemos una room** en la aplicación de GITTER.

    ![Postman1](https://i.imgur.com/oUUZ6pB.png)


2. Nos hubicaremos entonces en **POSTMAN**.
    
    Realizaremos un **GET** con el que recogeremos los parametros necesarios para realizar la eliminación de la sala que hemos creado anteriormente.

    Usaremos el la siente dirección:
    ```https://api.gitter.im/v1/rooms/```
    ![Postman2](https://i.imgur.com/7hQVXJ5.png)    
    
    De esta **recogeremos la id** de la sala.


3.  Para eliminar la sala solamente necesitamos el **id** recogida anteriormente.
    
    Añadiremos esa id a la anterior dirección:
    ```https://api.gitter.im/v1/rooms/``` **```ID-DE-LA-SALA```**
    ![Postman4](https://i.imgur.com/9joDhxS.png)
    
##### **PARAMETRO DE ENTRADA**
- Como parametro de entrada a la dirección que nos dan en la [API REST](https://developer.gitter.im/docs/rooms-resource) le añadiremos el parametro **id**, este párametro es una clave unica cifrada que pertenece a la sala en concreto.


##### **PARAMETRO DE SALIDA**

- Nos devuelve una verificación como parámetro de salida.
    ```
    {
        "success": true
    }
    ```
   
    
4. Finalmente podemos observar que la sala que hemos creado anteriormente ha desaparecido:
    
    ![Postman3](https://i.imgur.com/2AOHGbL.png)

