# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda práctica
# ===========================================================

# GRUPO:
# INTEGRANTE 1:
#   APELLIDOS, NOMBRE: JIMENEZ SANCHEZ BERNY
#   DNI: Y6177914J
# INTEGRANTE 2:
#   APELLIDOS, NOMBRE: OLIVA RAMIREZ RAFAEL
#   DNI:30251108J
# INTEGRANTE 3:
#   APELLIDOS, NOMBRE: ORTEGA CHINCHILLA ANTONIO VLADIMIR
#   DNI: 30266794J

# Para esta práctica, se pondrá en uso los conocimientos adquiridos sobre la OOP
# con la creación de un juego de cartas. Este juego de cartas es de dos jugadores
# y es llamado "UNO" y será un juego de tú contra la máquina. Si no sabes en qué
# consiste el juego "UNO", aquí te dejo un video: https://www.youtube.com/watch?v=MxnkDj8PIxQ&ab_channel=LIMITLESS

#Array de  numeros de las caratas  0,1,2,3,4,5,6,7,8,9
cardsArray = [0,1,2,3,4,5,6,7,8,9]
#Array de los colores
colors = ['Roja','Azul','Verde','Amarilla']
#Array cartas especiales +2,+4,cambio color, cambio de sentido, salto
especials = ['+2','+4','Cambio Color','Cambio de Sentido','Salto']
#Array Baraja Jugador
barajaJ = []
#Array Baraja IA
barajaI = []

#Clase de Barajas
class Baraja:
    #Funcion que creara la baraja de cada jugador
    def crearBaraja(self):
    #Funcion que te dice el tipo de carta
    def pintarCartas(self):
    #Funcion que verifica que la carta que posiste es la que tienes que poner
    def cumplirRegla(self):

#Clase de Jugadores
class Jugadores:
    #Funcion que te muestra tu baraja
    def mostrarMano(self, ):
    #Funcion de escoger color
    def escogerColor(self):
    #Funcion de robar cartas
    def robar(self):
    #Funcion que contrale los robos
    def controRobos(self):
    #Funcion para escoger carta y se aplique
    def escogerCarta(self):
    #Funcion que te reste un carta y verifique si es valida
    def condicCarta(self):

#Clase de la Mesa
class Mesa:
    #Funcion que te diga la ultima carta
    def ultiCarta(self):

#Comienza el juego


######################
#### GAME PLAY #######
######################
print("Welcome to UNO, let's begin...")

# Usa los conocimientos adquiridos junto con algo de lógica para jugar un juego de "UNO"!

# Recordad de nuevo el "Divide y Vencerás", primero debéis analizar las diferentes
# variales que van a afectaros, los posibles objetos que vayáis a necesitar,
# cuál es la interacción entre esos objetos y el cómo sería el gameplay como orquestador