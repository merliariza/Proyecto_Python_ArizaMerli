import json
import random

MY_DATABASE = 'puntajes.json'
HISTORIAL_DATABASE = 'nickname.json'


def cargarHistorial():
    try:
        with open(HISTORIAL_DATABASE, "r") as rf:
            historial = json.load(rf)
    except FileNotFoundError:
        historial = {}  
    return historial


def guardarHistorial(historial):
    with open(HISTORIAL_DATABASE, "w") as wf:
        json.dump(historial, wf, indent=4)

def cargarDatos():
    try:
        with open(MY_DATABASE, "r") as rf:
            datos = json.load(rf)
    except FileNotFoundError:
        datos = {"puntajes": {}} 
    return datos

def guardarDatos(datos):
    with open(MY_DATABASE, "w") as wf:
        json.dump(datos, wf, indent=4)

def registrarJugador(historial, nickname):
    if nickname not in historial:
        print(f'Bienvenido {nickname}')
        historial[nickname] = "jugador"
        guardarHistorial(historial)  
    else:
        print(f'{nickname} ya está registrado.')

def jugarRondaContraPC(usuario):
    juego = ['Piedra', 'Papel', 'Tijera']
    pc = random.choice(juego)
    print(f'La computadora eligió {pc}')
    if usuario not in juego:
        print('Ingrese un dato válido')
        return None
    elif usuario == pc:
        print('Es un empate')
        return 0 
    elif (usuario == 'Tijera' and pc == 'Papel') or (usuario == 'Papel' and pc == 'Piedra') or (usuario == 'Piedra' and pc == 'Tijera'):
        print('Felicidades, Ganó')
        return 2  
    else:
        print('Lo sentimos, esta vez ganó el PC')
        return -2  
    

def jugarRondaEntreJugadores(usuario1, usuario2):
    if usuario1 == usuario2:
        print('Es un empate')
        return 0 
    elif (usuario1 == 'Tijera' and usuario2 == 'Papel') or (usuario1 == 'Papel' and usuario2 == 'Piedra') or (usuario1 == 'Piedra' and usuario2 == 'Tijera'):
        print('Jugador 1 gana la ronda')
        return 2  
    else:
        print('Jugador 2 gana la ronda')
        return -2  


def registrarPuntaje(puntajes, nickname, puntos, maquina_puntos=0, escudo=False):
    nicknameS = str(nickname)  
    if nicknameS not in puntajes:
        puntajes[nicknameS] = {'puntos': 0, 'escudos': 0, 'puntos_maquina': 0}
    
    puntajes[nicknameS]['puntos'] += puntos
    puntajes[nicknameS]['puntos_maquina'] += maquina_puntos  # Almacenar puntos de la máquina
    if escudo:
        puntajes[nicknameS]['escudos'] += 1
    
    with open(MY_DATABASE, "w") as wf:
        json.dump(puntajes, wf, indent=4)

"""
def registrarPuntaje(puntajes, nickname, puntos, escudo=False):
    nicknameS = str(nickname)  
    if nicknameS not in puntajes:
        puntajes[nicknameS] = {'puntos': 0, 'escudos': 0}
    
    puntajes[nicknameS]['puntos'] += puntos
    if escudo:
        puntajes[nicknameS]['escudos'] += 1
    
    with open(MY_DATABASE, "w") as wf:
        json.dump(puntajes, wf, indent=4)
"""

def jugarConEscudoPC(nickname):
    datos = cargarDatos() 
    jugador_puntos = 0
    maquina_puntos = 0
    jugador_escudo = False
    victorias_consecutivas = 0
    ronda = 1

    while ronda <= 3 or (ronda > 3 and jugador_escudo):
        print(f"\n--- Ronda {ronda} ---")
        usuario = input('Elija Piedra, Papel o Tijera: ').capitalize()
        resultado = jugarRondaContraPC(usuario)

        if resultado is None:
            continue

        if resultado > 0:
            jugador_puntos += resultado
            victorias_consecutivas += 1
            
            if victorias_consecutivas == 2:
                print('¡Has ganado dos rondas consecutivas! Recibes un escudo.')
                jugador_escudo = True
                victorias_consecutivas = 0

        elif resultado < 0:
            maquina_puntos += -resultado 
            victorias_consecutivas = 0
            
            if jugador_escudo:
                print('Has perdido la ronda, tu escudo ha sido anulado.')
                jugador_escudo = False

        if ronda >= 3 and not jugador_escudo:
            break

        ronda += 1

    # Modificar aquí para incluir los puntos de la máquina
    registrarPuntaje(datos, nickname, jugador_puntos, maquina_puntos, escudo=jugador_escudo)

    print(f"\nResultados del juego:")
    print(f"Jugador: {jugador_puntos} puntos")
    print(f"Máquina: {maquina_puntos} puntos")
    
    if jugador_escudo:
        print("¡El jugador terminó con un escudo!")
    else:
        print("El jugador no tiene escudo.")


"""
def jugarConEscudoPC(nickname):
    datos = cargarDatos() 
    jugadorPuntos = 0
    maquinaPuntos = 0
    jugadorEscudo = False
    victoriasConsecutivas = 0
    ronda = 1

    while ronda <= 3 or (ronda > 3 and jugadorEscudo):
        print(f"\n--- Ronda {ronda} ---")
        usuario = input('Elija Piedra, Papel o Tijera: ').capitalize()
        resultado = jugarRondaContraPC(usuario)

        if resultado is None:
            continue

        if resultado > 0:
            jugadorPuntos += resultado
            victoriasConsecutivas += 1
            
            if victoriasConsecutivas == 2:
                print('¡Has ganado dos rondas consecutivas! Recibes un escudo.')
                jugadorEscudo = True
                victoriasConsecutivas = 0

        elif resultado < 0:
            maquinaPuntos += -resultado 
            victoriasConsecutivas = 0
            
            if jugadorEscudo:
                print('Has perdido la ronda, tu escudo ha sido anulado.')
                jugadorEscudo = False

        if ronda >= 3 and not jugadorEscudo:
            break

        ronda += 1

    registrarPuntaje(datos, nickname, jugadorPuntos, escudo=jugadorEscudo)

    print(f"\nResultados del juego:")
    print(f"Jugador: {jugadorPuntos} puntos")
    print(f"Máquina: {maquinaPuntos} puntos")
    
    if jugadorEscudo:
        print("¡El jugador terminó con un escudo!")
    else:
        print("El jugador no tiene escudo.")
"""

def jugarConEscudoDosJugadores(nickname1, nickname2):
    datos = cargarDatos()
    jugador1Puntos = 0
    jugador2Puntos = 0
    jugador1Escudo = False
    victoriasConsecutivas = 0
    ronda = 1

    while ronda <= 3 or (ronda > 3 and jugador1Escudo):
        print(f"\n--- Ronda {ronda} ---")
        usuario1 = input('Jugador 1 elija Piedra, Papel o Tijera: ').capitalize()
        usuario2 = input('Jugador 2 elija Piedra, Papel o Tijera: ').capitalize()
        resultado = jugarRondaEntreJugadores(usuario1, usuario2)

        if resultado > 0: 
            jugador1Puntos += resultado
            victoriasConsecutivas += 1

            if victoriasConsecutivas == 2:
                print('¡Jugador 1 ha ganado dos rondas consecutivas! Recibe un escudo.')
                jugador1Escudo = True
                victoriasConsecutivas = 0

        elif resultado < 0:  
            jugador2Puntos += -resultado  
            victoriasConsecutivas = 0

            if jugador1Escudo:
                print('Jugador 1 perdió la ronda, su escudo ha sido anulado.')
                jugador1Escudo = False

        if ronda >= 3 and not jugador1Escudo:
            break

        ronda += 1

   
    registrarPuntaje(datos, nickname1, jugador1Puntos, escudo=jugador1Escudo)
    registrarPuntaje(datos, nickname2, jugador2Puntos, escudo=False)

  
    print(f"\nResultados del juego:")
    print(f"Jugador 1: {jugador1Puntos} puntos")
    print(f"Jugador 2: {jugador2Puntos} puntos")

    if jugador1Escudo:
        print("¡Jugador 1 terminó con un escudo!")
    else:
        print("Jugador 1 no tiene escudo.")