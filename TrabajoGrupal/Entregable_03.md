# Post
El método **POST** es usado cuando se requiere enviar información al servidor como, por ejemplo, un archivo de actualización, información de formulario, etc. En otras palabras, éste método se usa cuando se necesita enviar una entidad para algún recurso determinado.

## Primer Post 
En el primer post utilizaremos la [API TRELLO](https://developer.atlassian.com/cloud/trello/). Lo que estamos haciendo es crear una lista en un tablero trello.

 1. Primero tendremos que obtener el id de la tabla que se ubica en la url de la tabla *https://trello.com/b/**KF4hyh3s**/pepe*.
![enter image description here](https://i.imgur.com/7BcCTt8.png)

 2. Le hacemos  la petición a esta url *https://api.trello.com/1/boards/KF4hyh3s/lists*. 
![enter image description here](https://i.imgur.com/pXPASgu.png)

### **PARAMETRO DE ENTRADA**
 - key: **String** *Es la clave de seguridad para autenticar el usuario. Aqui es donde se consigue [link](https://trello.com/app-key)*
 - token: **String** *Es el token de seguridad para autenticar el usuario. Aqui es donde se consigue [link](https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=Server%20Token&key=6e1e48f5edf778c578dcf3d9a64739fc)*
 - name: **String** *Es el nombre de la lista quu añadiremos.*
### **PARAMETRO DE SALIDA**
- id: **String** *Id de la lista.*
- name: **String** *Nombre de la lista.*
- closed: **Boolean** *True si la lista esta cerrada o False si no esta cerrada.*
- pos: **Double** *Posición de la lista.*
- idBoard: **String** *Id de la tabla donde se crea la lista.*
- limits: **Array** *Limite de elementos que se puede añadir a la lista.*


3. Como resultado final se agrego la lista de forma correcta.![enter image description here](https://i.imgur.com/Az3QWCl.png)
