import json

MY_DATABASE = 'nickname.json'
PUNTAJES_DATABASE = 'puntajes.json'

def cargarHistorial():
    try:
        with open(MY_DATABASE, "r") as rf:
            historial = json.load(rf)
    except FileNotFoundError:
        historial = {}  
    return historial

def guardarHistorial(historial):
    with open(MY_DATABASE, "w") as wf:
        json.dump(historial, wf, indent=4)

def cargarDatos():
    try:
        with open(MY_DATABASE, "r") as rf:
            datos = json.load(rf)
    except FileNotFoundError:
        datos = {"jugadores": {}} 
        guardarDatos(datos)  
    return datos


def guardarDatos(datos):
    with open(PUNTAJES_DATABASE, "w") as wf:
        json.dump(datos, wf, indent=4)

def validarApodo(nickname, historial):
    if nickname not in historial:
        return True
    else:
        print('Este apodo ya fue usado, ingrese un nuevo apodo.')
        return False

def ingresarDos(historial):
    nickname1 = input('Ingrese el apodo del jugador #1: ')
    if nickname1 not in historial:
        print(f'Bienvenido {nickname1}, es el jugador #1')
        historial[nickname1] = "jugador #1"
    else:
        input('Este apodo ya fue usado, ingrese un nuevo apodo')
        return None  

    nickname2 = input('Ingrese el apodo del jugador #2: ')
    if nickname2 not in historial:
        print(f'Bienvenido {nickname2}, es el jugador #2')
        historial[nickname2] = "jugador #2"
    else:
        input('Este apodo ya fue usado, ingrese un nuevo apodo')
        return None  

    guardarHistorial(historial)

    return nickname1, nickname2  

def ingresarUno(historial):
    while True:
        nickname = input('Ingrese el apodo del jugador: ')
        if validarApodo(nickname, historial):
            print(f'Bienvenido {nickname}')
            historial[nickname] = "jugador"
            guardarHistorial(historial)
            break  

def actualizarPuntosIA(nicknameIa, rondasGanadas):
    datos = cargarDatos()
    if nicknameIa not in datos["jugadores"]:
        datos["jugadores"][nicknameIa] = {"puntos": 0, "escudos": 0}

    datos["jugadores"][nicknameIa]["puntos"] += 2 * rondasGanadas  
    guardarDatos(datos)

def jugarTresRondas():
    datosJuego = cargarHistorial()  
    nickname = input("Ingrese su nickname: ")
    while not validarApodo(nickname, datosJuego):
        nickname = input("Ingrese un nuevo nickname: ")
    print(f"Nickname {nickname} válido. ¡Inicia el juego!")
    