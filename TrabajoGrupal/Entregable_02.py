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


#Array de los colores
colors = ['Negra','Roja','Azul','Verde','Amarilla']
# Array de la  baraja de cartas sin cojer
baraja = []
# Array del montón en la mesa
monton = []
#Array de los dos jugadores del Jugador y de la IA
jugadores = [
    {"nombre": "", "mano": [], "tipo": "HUMANO"},
    {"nombre": "JuanIA", "mano": [], "tipo": "IA"}
]

#Clase de Barajas
class Baraja:
    #Funcion que creara la baraja de cada jugador
    def crearBaraja(self):
    #Funcion que te dice el tipo de carta
    def pintarCartas(self):
    #Funcion que comprueba si la carta es especial, es decir, Negra
    def cumplirRegla(self):


#Clase de Jugadores
class Jugadores:

    #Funcion que te muestra tu baraja
    def mostrarMano(self):

    #Funcion de escoger color
    def escogerColor(self):
        #Variable donde se almacenara el color elegido
        colorElegido = ""
        #Variable para controlar el bucle
        control = True
        while control:
            #Variable de la posicion del array de los colores
            cont_colors = 1#Es 1 para que no coja el color negro
            for c in colors[1:]:
                print(f'{c}.{str(cont_colors)} ')   
                cont_colors +1
            #Le pedimos al usuario que elija el color con un numero
            colorElegido = input("Escoge color: ")
            #El bucle se termina cuando sea elegido un numero, no sea elegido el negro y si no te has pasado de rango
            if(colorElegido.isnumeric() and int(colorElegido) > 0 and int(colorElegido) <= len(colors) - 1):
                control = False
        #Retornamos el color con la posicion en el array
        return colors[int(colorElegido)]

    #Funcion de robar cartas
    #
    #     La función robar, utilizará
    #
    def robar(jugador, numero, baraja):
        #Este bucle usa un elemento comodín "_" que no va a tener utilidad || Podría ser una variable como "ì", "x", etc .
        for _ in range(numero):
            #Se ejecutará si hay cartas en la baraja.
            if len(baraja) > 0:
                #Gracias al método "append" agregaremos a la mano de jugador una la carta en posición 0 de la baraja.
                jugador["mano"].append(baraja[0])
                #Una vez cogida la carta de la baraja le restaremos a la misma una.
                baraja = baraja[1:]
        #Retornamos la baraja.
        return baraja

    #Funcion que contrale los robos
    def controRobos(self):

    #Funcion para escoger carta y se aplique
    def escogerCarta(self):
    #Funcion con la que se activa la carta
    def jugarCarta(self):

######################
#### GAME PLAY #######
######################
#Con esta funcion se iniciara el programa
def start():
    print("Welcome to UNO, let's begin...")

# Usa los conocimientos adquiridos junto con algo de lógica para jugar un juego de "UNO"!

# Recordad de nuevo el "Divide y Vencerás", primero debéis analizar las diferentes
# variales que van a afectaros, los posibles objetos que vayáis a necesitar,
# cuál es la interacción entre esos objetos y el cómo sería el gameplay como orquestador