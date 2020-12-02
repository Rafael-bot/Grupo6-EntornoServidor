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

# Importamos la lib random
import random
# Array de los colores
colors = ['Negra', 'Azul', 'Verde', 'Roja', 'Amarilla']
# Array de la  baraja de cartas sin cojer
baraja = []
# Array del montón en la mesa
monton = []

# Clase de Barajas
class Baraja:
    # Funcion que creara la baraja de cada jugador
    def crearBaraja(self):
        baraja = []  # este array vacio pide al usuario que introduzca la baraja
        for carta in range(0, 9):  # aqui le damos valores a tomar desde el 0 al 9
            for color in colors[1:]:
                for _ in range(2 if carta > 0 else 1):
                    baraja.append(
                        {"color": color, "valor": str(carta), "robar": 0})
        for _ in range(4):  # Añadimos las cartas especiales
            baraja.append({"color": "Negra", "valor": "+4", "robar": 4})
            # nos permite agregar nuevas cartas a la baraja
            baraja.append({"color": "Negra", "valor": "CAMBIO_COLOR", "robar": 0})

        for _ in range(3):  # Añadimos las cartas de +2
            for color in colors[1:]:
                # nos permite agregar nuevas cartas a la baraja
                baraja.append({"color": color, "valor": "+2", "robar": 2})
                baraja.append(
                    {"color": color, "valor": "CAMBIO_SENTIDO", "robar": 0})
                baraja.append({"color": color, "valor": "BLOQUEO", "robar": 0})
        random.shuffle(baraja)  # reorganiza el orden de la baraja
        return baraja

    def pintarCarta(self,carta):  # esta funcion indica el tipo de carta que es de la variable carta le da un color y un valor
        return ((carta["color"] + " ") if carta["color"] != "Negra" else "") + carta["valor"] + (
        # retorna un calor y un numero
            "(" + str(carta["robar"]) + ")" if carta["robar"] > 0 else "")
        # Funcion que comprueba si la carta es especial, es decir, Negra

    def cumpleLasReglas(self, cartaEscogida, cartaEnMesa):
        # si la carta tiene color y tipo negro cumple una funcion especifica
        if cartaEscogida["color"] == "Negra":
            return True
        else:  # sino es negro definirme cual es e imprime que valor y color tiene
            return cartaEnMesa["color"] == cartaEscogida["color"] or cartaEnMesa["valor"] == cartaEscogida["valor"]


# Clase de Jugadores
class Jugadores:
    # Funcion que te muestra tu baraja
    # el atributo controlIA para mostrar la baraja si es un jugador, si es false es la IA  y si es true es el jugador
    # el atributo cardMesa para pintar la ultima carata de la mesa
    def mostrarMano(self, jugador, control_ia=False, card_mesa=None):
        i = 1 # Variable que enumera las cartas del mazo
        col = 0 # Variable que hace los saltos de lineas
        cadenaSalida = "" # Variable del resultado de la funcion. Es la cadena de salida
        for carta in jugador["mano"]: # Bucle con el que iremos añadiendo las cartas del mazo del jugador a la variable result
            # Variable donde vamos guardando las cartas
            textoCarta = ((str(i) + ". " if control_ia else "")) # Si la variable controlIA es true significa que es el mazo del jugador y se imprimira, si no es de la IA no imprimira nada
            # Le añadimos la carta con la funcion pintar carta que retornara la carta
            if card_mesa != None and Baraja().cumpleLasReglas(carta, card_mesa):
                textoCarta += Baraja().pintarCarta(carta)
            else:
                textoCarta += Baraja().pintarCarta(carta)
            # Le añadimos el salto de linea
            cadenaSalida += ("\t" if col > 0 else "\r\n") + textoCarta.ljust(20, " ")# Le añadimos un tabulador con la carta y el ljust le añadimos 15 espacios si se cumple la condicion
            if (col == 3):#4 Columnas
                col = 0# Le ponemos otra vez el valor a cero para la siguiente fila, para que haga el salto de linea
            else:
                col += 1
            i += 1
        # Imprimimos el resultado
        print(cadenaSalida)

    # Funcion de escoger color
    def escogerColor(self):
        # Variable donde se almacenara el color elegido
        colorElegido = ""
        # Variable para controlar el bucle
        control = True
        while control:
            # Variable de la posicion del array de los colores
            cont_colors = 1  # Es 1 para que no coja el color negro
            for c in colors[1:]:
                print(f'{c}.{str(cont_colors)} ')
                cont_colors += 1
            # Le pedimos al usuario que elija el color con un numero
            colorElegido = input("Elige color: ")
            # El bucle se termina cuando sea elegido un numero, no sea elegido el negro y si no te has pasado de rango
            if (colorElegido.isnumeric() and int(colorElegido) > 0 and int(colorElegido) <= len(colors) - 1):
                control = False
        # Retornamos el color con la posicion en el array
        return colors[int(colorElegido)]

    # Funcion de robar cartas
    #
    #     La función robar, utilizará
    #
    def robar(self, jugador, numero, baraja):
        # Este bucle usa un elemento comodín "_" que no va a tener utilidad || Podría ser una variable como "ì", "x", etc .
        for _ in range(numero):
            # Se ejecutará si hay cartas en la baraja.
            if len(baraja) > 0:
                # Gracias al método "append" agregaremos a la mano de jugador una la carta en posición 0 de la baraja.
                jugador["mano"].append(baraja[0])
                # Una vez cogida la carta de la baraja le restaremos a la misma una.
                baraja = baraja[1:]
        # Retornamos la baraja.
        return baraja

    # Funcion que contrale los robos
    def controlaRobos(self, jugador, cartaMesa, baraja):
        # Si el valor de la carta es +4 robara 4 cartas
        if (cartaMesa["valor"] == "+4"):
            print('ROBA 4 CARTAS.')
            # Variable donde le guardamos la baraja actualizada
            baraja = self.robar(jugador, 4, baraja)
            # Le damos el valor de robo 0, para marcar que esa carta se ha tirado, ya que esta en la mesa
            cartaMesa["robar"] = 0
        # Si el valor de la carta es +2 y el valor de robo de la carta es mayor que 0
        elif (cartaMesa["valor"] == "+2" and cartaMesa["robar"] > 0):
            # Variable booleana que utilizaremos para tirar los mismos mas dos
            masdoses = False
            # Bucle que recorre el mazo del jugador para tirar todos los mismos +2 del mazo
            for carta in jugador["mano"]:
                masdoses = masdoses or carta["valor"] == '+2'  # Si la cartar tiene como valor +2 dara true
            # Solo entrara si masdoses es false, porque significa que no ha encontrado mas +2
            if not masdoses:
                # Imprimimos el numeros de cartas a robar
                print(f'ROBA -> {str(cartaMesa["robar"])} CARTAS.')
                # le guardamos la baraja actualizada
                baraja = self.robar(jugador, cartaMesa["robar"], baraja)
                # Le damos el valor de robo 0, para marcar que esa carta se ha tirado, ya que esta en la mesa
                cartaMesa["robar"] = 0
        # Retornamos la baraja actualizada
        return baraja

    # Funcion para escoger carta y se aplique
    def escogerCarta(self, jugador, cartaEnMesa, baraja):

        # Variable que controla el bucle while.
        control_bucle = True

        # Bucle que controla la funcion escogerCarta.
        while control_bucle:
            # Recogemos la funcion mostrarMano y sus datos.
            self.mostrarMano(jugador, True, cartaEnMesa)
            # Pintamos la ultima del monton en la mesa.
            print("\nCarta de la mesa: ", Baraja().pintarCarta(monton[-1]))
            # Escogemos la carta. || .capitalize() convierte la primera letra en mayusculas.
            idCartaEscogida = input("Escoge la carta que tiraras (R para robar " + str(len(baraja)) + "):").capitalize()
            # idCartaEscogida = input(f'Escoge la carta que tiraras (R) Robar{str(len(baraja))}:').capitalize()
            # Condicion si pulsas R, mientras existan cartas en la baraja la robas si no no se pueden robar.
            if idCartaEscogida == "R":
                if len(baraja) > 0:
                    baraja = self.robar(jugador, 1, baraja)
                else:
                    print("NO QUEDAN CARTAS EN LA BARAJA!")
            # Si la carta escogida es numerica y el numero mayor que 0, y es el numero es menor o igual al tamaño de la mano de jugador se ejecutará lo siguiente:
            elif idCartaEscogida.isnumeric() and int(idCartaEscogida) > 0 and int(idCartaEscogida) <= len(jugador["mano"]):
                # Variable que recogera la ultima carta que se encuentra en la mano del jugador.
                cartaEscogida = jugador["mano"][int(idCartaEscogida) - 1]
                # Condicion control de reglas.
                if Baraja().cumpleLasReglas(cartaEscogida, cartaEnMesa):
                    # Sobre escribir la mano del jugador.
                    jugador["mano"] = jugador["mano"][0:int(idCartaEscogida) - 1] + jugador["mano"][int(idCartaEscogida):]
                    # Si la carta es especial y de escoger color, se realiza la función escogerColor y se para el bucle.
                    if (cartaEscogida["color"] == "Negra"):
                        cartaEscogida["color"] = self.escogerColor()
                    control_bucle = False
                else:
                    print("CARTA NO VALIDA")
        # Retornamos la cartaEscogida y la baraja.
        return cartaEscogida, baraja

    # Funcion con la que se activa la carta
    def jugarCarta(self,jugador, cartaEnMesa, baraja):

        control_bucle = True

        while control_bucle:
            # Muestra el numero de cartas del jugador.
            print("Tiene " + str(len(jugador["mano"])) + " cartas")
            # Array de cartas validas.
            cartasValidas = []
            # Variable que colores.
            cartasColor = {}

            # Bucle que que comprueba que las cartas son validas.
            for i, carta in enumerate(jugador["mano"]):
                if Baraja().cumpleLasReglas(carta, cartaEnMesa):
                    cartasValidas.append(i)
                if carta["color"] != "Negra":
                    if carta["color"] in cartasColor:
                        cartasColor[carta["color"]] += 1
                    else:
                        cartasColor[carta["color"]] = 1

            # SIENDO LAS CARTAS VÁLIDAS.
            # Variable de control.
            idCartaSeleccionada = -1
            # Condicion para robar carta si el jugador no tiene cartas válidas.
            if len(cartasValidas) == 0:
                if len(baraja) > 0:
                    print("\tROBO UNA CARTA")
                    baraja = self.robar(jugador, 1, baraja)
                else:
                    print("NO HAY CARTAS")
                    # Definir que no existe cartas para robar
                    # Devolvemos nada y la baraja.
                    return None, baraja
            # Escogemos las que dan mayor ventaja.
            else:
                # Bucle control de cartas en el que guardamos las cartas por el id.
                for idCarta in cartasValidas:
                    # Guardamos los id carta en idCartaSeleccionada
                    if idCartaSeleccionada < 0:
                        idCartaSeleccionada = idCarta
                    else:
                        if not jugador["mano"][idCarta]["valor"].isnumeric():
                            idCartaSeleccionada = idCarta
                # Si en la mano del jugador el id es el de una carta especial (NEGRO)
                if jugador["mano"][idCartaSeleccionada]["color"] == "Negra":
                    color = ""
                    colorNumero = 0
                    # Recogemos color de las cartas y le asignamos un numero.
                    for c in cartasColor:
                        if cartasColor[c] > colorNumero:
                            colorNumero = cartasColor[c]
                            color = c
                    # Asignamos el color a la mano del jugador.
                    jugador["mano"][idCartaSeleccionada]["color"] = c
                #Salimos de bucle.
                control_bucle = False
        # Asignamos los datos del jugador a la variable.
        cartaEscogida = jugador["mano"][idCartaSeleccionada]
        # La mano se conforma desde el elemendo 0 hasta el ultimo mas, los elementos numericos que suman del 1: "infinito".
        jugador["mano"] = jugador["mano"][0:int(idCartaSeleccionada)] + jugador["mano"][int(idCartaSeleccionada) + 1:]
        # Devolvemos.
        return cartaEscogida, baraja

######################
#### GAME PLAY #######
######################
# Con esta funcion se iniciara el programa
def start():

    baraja = Baraja().crearBaraja()#Llenamos la baraja

    #Lista de jugadores
    jugadores = [
        {"nombre": "", "mano": [], "tipo": "HUMANO"},
        {"nombre": "RichardIA", "mano": [], "tipo": "IA"}
    ]
    #El usuario introduce su nombre en el juego
    jugadores[0]["nombre"] = input("Dime tu nombre:")
    #Bucle que reparte las cartas de la baraja a cada jugador
    for _ in range(7):
        for jugador in jugadores:
            jugador["mano"].append(baraja[0])#Añadimos la carta al jugador
            baraja = baraja[1:]

    monton.append(baraja[0])#Sacamos la primera carta a la mesa
    baraja = baraja[1:]#Guardamos el resto de cartar al mazo
    if (monton[0]["color"] == "Negra"):
        monton[0]["color"] = random.choice(colors[1:])

    continuar = True #Variable que controla si la partida termina o no
    idJugador = 0 #Variable que controla que selecciona el jugador
    direccionJuego = +1 #Varaible que controla al direccion de la partida
    numeroJugadores = len(jugadores) #Variable de numeros de jugadores

    while continuar:#Partida

        if len(baraja) <= 0:#Si la baraja no tienes mas cartas se a terminado la partida
            continuar = False #Termina la partida
        if monton[-1]["valor"] == "SALTO":
            idJugador += direccionJuego
            idJugador = (numeroJugadores + idJugador) if idJugador < 0 else idJugador % numeroJugadores
        jugador = jugadores[idJugador]
        print("\r\nTurno de " + jugador["nombre"])
        baraja = Jugadores().controlaRobos(jugador, monton[-1], baraja)#Controlamos la sumas de robos d
        # e +2 y +4 con la funcion controlaRobos
        #Solo IA
        if jugador["tipo"] == "IA":
            #DIrectamente selecciona la carta automaticamente con la funcion jugarCarta
            cartaEscogida, baraja = Jugadores().jugarCarta(jugador, monton[-1], baraja)
            print("\tTira " + Baraja().pintarCarta(cartaEscogida))#La pinta con la funcion pintaCarta
        else:#Jugador
            cartaEscogida, baraja = Jugadores().escogerCarta(jugador, monton[-1], baraja)#Seleccionamos la carta. Retorna la carta elegida y la baraja actualizada
        if cartaEscogida != None:
            cartaEscogida["robar"] += monton[-1]["robar"]
            monton.append(cartaEscogida)#Añadimos las cartas +2 o +4 al mazo de la mesa
        if len(jugador["mano"]) == 0:
            continuar = False
            print(jugador["nombre"] + "  GANA LA PARTIDA")#Gana el jugador
        if monton[-1]["valor"] == "CAMBIO":
            direccionJuego *= -1
        idJugador += direccionJuego
        idJugador = (numeroJugadores + idJugador) if idJugador < 0 else idJugador % numeroJugadores

# Usa los conocimientos adquiridos junto con algo de lógica para jugar un juego de "UNO"!

# Recordad de nuevo el "Divide y Vencerás", primero debéis analizar las diferentes
# variales que van a afectaros, los posibles objetos que vayáis a necesitar,
# cuál es la interacción entre esos objetos y el cómo sería el gameplay como orquestador

start()