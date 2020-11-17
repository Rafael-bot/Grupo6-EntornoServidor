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
    baraja = []  # este array vacio pide al usuario que introduzca la baraja
    for carta in range(0, 9):  # aqui le damos valores a tomar desde el 0 al 9
        for color in colores[1:]:
            for _ in range(2 if carta > 0 else 1):
                baraja.append(
                    {"color": color, "valor": str(carta), "robar": 0})
    for _ in range(4):  # Añadimos las cartas especiales
        baraja.append({"color": "NEGRO", "valor": "+4", "robar": 4})
        # nos permite agregar nuevas cartas a la baraja
        baraja.append({"color": "NEGRO", "valor": "CAMBIO_COLOR", "robar": 0})

    for _ in range(3):  # Añadimos las cartas de +2
        for color in colores[1:]:
            # nos permite agregar nuevas cartas a la baraja
            baraja.append({"color": color, "valor": "+2", "robar": 2})
            baraja.append(
                {"color": color, "valor": "CAMBIO_SENTIDO", "robar": 0})
            baraja.append({"color": color, "valor": "BLOQUEO", "robar": 0})
    rd.shuffle(baraja)  # reorganiza el orden de la baraja
    return baraja

    #Funcion que te dice el tipo de carta
    def pintarCartas(self):
    #Funcion que comprueba si la carta es especial, es decir, Negra
    def cumplirRegla(self):


#Clase de Jugadores
class Jugadores:

    #Funcion que te muestra tu baraja
    # el atributo controlIA para mostrar la baraja si es un jugador, si es false es la IA  y si es true es el jugador
    # el atributo cardMesa para pintar la ultima carata de la mesa
    def mostrarMano(self, jugador, control_ia=False, card_mesa=None):
        # Variable que enumera las cartas del mazo
        enum_mazo = 1
        # Variable que hace los saltos de lineas
        cont_column = 0
        # Variable del resultado de la funcion. Es la cadena de salida
        result = ''
        # Bucle con el que iremos añadiendo las cartas del mazo del jugador a la variable result
        for card in jugador['mano']:
            #Si la variable controlIA es true significa que es el mazo del jugador y se imprimira, si no es de la IA no imprimira nada
            if(control_ia):
                # Variable donde vamos guardando las cartas
                carta_mazo = f'{str(enum_mazo)}. '
            else:
                carta_mazo = ''
            #Le añadimos la carta con la funcion pintar carta que retornara la carta
            carta_mazo += Baraja.pintarCarta(card)
            if(cont_column > 0):
                result+=f'\t{carta_mazo.ljust(15, " ")}'#Le añadimos un tabulador con la carta y el ljust le añadimos 15 espacios
            else:
                result+=f'\n{carta_mazo.ljust(15, " ")}'#Le añadimos el salto de linea
            #Si la variable del contador de las columnas llega a 2 significa que se ha agregado las 3 columnas
            if (cont_column == 2):
                cont_column = 0 #Le ponemos otra vez el valor a cero para la siguiente fila, para que haga el salto de linea
            else:
                cont_column += 1
            enum_mazo += 1
        #Imprimimos el resultado
        print(result)

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
                cont_colors +=1
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
    def robar(self, jugador, numero, baraja):
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
