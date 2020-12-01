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


## Segundo Post 
En el segundo post utilizaremos la [API GITTER](https://developer.gitter.im/docs/welcome). Lo que estamos haciendo es enviar un mensaje en una sala. Para poder hacer las peteciones a esta api, necesitamos autenticarnos con el OAuth2.0 ![enter image description here](https://i.imgur.com/Da2x5Zu.png)
Obtenemos el token en este [link](https://developer.gitter.im/apps).


 1. Primero tendremos que obtener el id de la room que se obtiene con  que se obtiene con la peticion 
 `GET https://api.gitter.im/v1/rooms/`.
![enter image description here](https://i.imgur.com/XwmDrlY.png)

 2. Le hacemos  la petición a esta url *https://api.gitter.im/v1/rooms/5fc4d04fd73408ce4ff54ae5/chatMessages*. 
![enter image description here](https://i.imgur.com/qGVqWTT.png)

### **PARAMETRO DE ENTRADA**
 - status: **Boolean** *True si el mensaje esta actualizado **NO SE PUEDE ACTUALIZAR** y False si el mensaje no esta actualizado **SI SE PUEDE ACTUALIZAR**.*

### BODY
 - text: **String** *Texto por el que se va a actualizar el mensaje.*
 `{"text":"Mensaje enviado desde postman"}`
	 

### **PARAMETRO DE SALIDA**
- id: **String** *Id del mensaje	.*
- text: **String** *Nombre de la lista.*
- html: **String** *Html del mensaje.*
- sent: **String** *Fecha en la que se envió el mensaje.*
- unread: **Boolean** *True significa que no se a leído y False es que si se ha leído.*
- readBy: **Int** *Números de usuario que han leído el mensaje.*
- urls:**Array**  *Urls del mensaje.*
- mentions:**Array** *Usuarios que hemos mencionado en el mensaje.*
- issues:**Array**
- meta:**Array**
- v:**Int**
- fromUser:**Objeto**
	- id:**String** *Id del usuario.*
	- username:**String** *Nombre del usuario.*
	- displayName:**String** *Nombre del usuario.*
	- url:**String** *Url del usuario.*
	- avatarUrl:**String** *Url de la imagen del usuario.*
	- avatarUrlSmall:**String** *Url dela imagen del usuario tamaño pequeño.*
	- avatarUrlMedium:**String** *Url dela imagen del usuario tamaño medio.*
	- v:**Int**
	- gv:**String**


3. Como resultado se envió el mensaje correctamente.![enter image description here](https://i.imgur.com/ZrTCm46.png)

# GET
El método **Get** significa recuperar cualquier información (en forma de una entidad) identificada por el Request-URI.

## Primer Get 
En el primer get utilizaremos la [API SPOTIFY](https://developer.spotify.com/documentation/web-api/). Lo que haremos sera realizr diferentes consultas a un usuario logado sin necesidad de introducir codigo.

### **PARAMETRO DE ENTRADA**
- **Authorization:** Requerido. Un token de acceso válido del servicio de cuentas de Spotify: consulte la Guía de autorización de API web para obtener más detalles. 		El token de acceso debe haber sido emitido en nombre de un usuario. El token de acceso debe tener el user-read-playback-statealcance autorizado para poder leer la            información.
### **PARAMETRO DE SALIDA**
- Una solicitud exitosa devolverá un **200 OK** código de respuesta con una carga útil json que contiene los objetos del dispositivo. Cuando no se                  	      encuentran dispositivos disponibles, la solicitud devolverá una respuesta **200 OK** con una lista de dispositivos vacía.
	
Como resultado se envió el mensaje correctamente.![enter image description here](https://i.imgur.com/zdI2zZz.jpg)

## Segundo Get 
En el primer get utilizaremos la [API SPOTIFY](https://developer.spotify.com/documentation/web-api/). Lo que haremos sera realizar diferentes consultas a un usuario logado sin necesidad de introducir codigo.

### **PARAMETRO DE ENTRADA**
**Se obtienen las pistas disponibles de un album**
- **OFFSET:**	Opcional . El índice de la primera pista que se devuelve. Por defecto: 0 (el primer objeto). Úselo con límite para obtener el siguiente conjunto de pistas.
- **LIMIT:** Opcional . El número máximo de pistas para regresar. Predeterminado: 20. Mínimo: 1. Máximo: 50.
- **MARKET:** Opcional . Un código de país ISO 3166-1 alpha-2 o la cadena from_token. Proporcione este parámetro si desea aplicar Track Relinking .
- **ID:** El ID de Spotify del álbum.
- **Authorization:** Requerido. Un token de acceso válido del servicio de cuentas de Spotify: consulte la Guía de autorización de API web para obtener más detalles.
### **PARAMETRO DE SALIDA**
- En caso de éxito, el código de estado HTTP en el encabezado de la respuesta es **200** correcto y el cuerpo de la respuesta contiene una matriz de objetos de seguimiento simplificados (envueltos en un objeto de paginación ) en formato JSON. En caso de error, el código de estado del encabezado es un código de error y el cuerpo de la respuesta contiene un objeto de error .
	
Como resultado se envió el mensaje correctamente.![enter image description here](https://i.imgur.com/1gwbIVQ.jpg)

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

# PUT
El método **Put** Crea un nuevo elemento o reemplaza una representación del elemento de destino con los datos de la petición.

## PRIMER PUT 
En el primer PUT utilizaremos la [API SPOTIFY](https://developer.spotify.com/documentation/web-api/). Lo que haremos sera realizar diferentes consultas a un usuario logado sin necesidad de introducir codigo.

### **PARAMETRO DE ENTRADA**
**Cambiar los detalles de una lista de Reproduccion**
 - **Playlist_id:** El ID de Spotify para la lista de reproducción.

- **Authorization:** Requerido . Un token de acceso válido del servicio de cuentas de Spotify. El token de acceso debe haber sido emitido en nombre del usuario.
Cambiar una lista de reproducción pública para un usuario requiere la autorización del playlist-modify-publicalcance; cambiar una lista de reproducción privada requiere el playlist-modify-privatealcance. 

- **Tipo de contenido:** Requerido. El tipo de contenido del cuerpo de la solicitud:application/json

### **PARAMETRO DE SALIDA**
- En caso de éxito, el código de estado HTTP en el encabezado de respuesta es **200** correcto. En caso de error, el código de estado del encabezado es un código de error y el cuerpo de la respuesta contiene un objeto de error . Intentar cambiar una lista de reproducción cuando no tiene la autorización del usuario devuelve el error **403** Prohibido.
	
Como resultado se envió el mensaje correctamente.![enter image description here](https://i.imgur.com/NQWepbI.jpg)

Se corrobora resultado
![enter image description here](https://i.imgur.com/vqHQb0j.jpg)
